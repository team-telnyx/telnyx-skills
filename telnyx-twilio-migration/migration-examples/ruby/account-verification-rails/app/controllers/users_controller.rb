class UsersController < ApplicationController
  def new
    @user = User.new
  end

  def show
    @user = current_user
  end

  def create
    @user = User.new(user_params)
    if @user.save
      # Save the user_id to the session object
      session[:user_id] = @user.id

      # Create verification profile using Telnyx Verify API
      begin
        # Initialize Telnyx client
        telnyx = Telnyx::Client.new(api_key: ENV['TELNYX_API_KEY'])
        
        # Create a verify profile for this user
        phone_number = "#{@user.country_code}#{@user.phone_number}"
        profile_name = "user_#{@user.id}_#{Time.now.to_i}"
        
        verify_profile = telnyx.verify_profiles.create(
          name: profile_name,
          sms: {
            enabled: true,
            template: "Your verification code is: %code%. This code will expire in %time_limit% minutes."
          }
        )
        
        # Store the verify profile ID
        @user.update(authy_id: verify_profile.id)
        
        # Send verification code via SMS
        verification = telnyx.verifications.trigger_sms(
          phone_number: phone_number,
          verify_profile_id: verify_profile.id,
          timeout_secs: 300
        )
        
        flash[:notice] = "Verification code sent to #{phone_number}"
        Rails.logger.info("Verification #{verification.id} sent to #{phone_number}")
      rescue StandardError => e
        Rails.logger.error("Telnyx Verify error: #{e.message}")
        Rails.logger.error(e.backtrace&.first(5)&.join("\n"))
        flash[:alert] = "Could not send verification code: #{e.message}"
      end

      redirect_to verify_path
    else
      render :new
    end
  end

  def show_verify
    return redirect_to new_user_path unless session[:user_id]
  end

  def verify
    @user = current_user

    begin
      # Initialize Telnyx client
      telnyx = Telnyx::Client.new(api_key: ENV['TELNYX_API_KEY'])
      
      # Find the most recent verification for this phone number
      phone_number = "#{@user.country_code}#{@user.phone_number}"
      
      # List recent verifications for this phone number
      verifications_response = telnyx.verifications.by_phone_number.list(phone_number)
      
      if verifications_response&.data&.any?
        # Get the most recent verification
        latest_verification = verifications_response.data.first
        
        # Verify the code
        result = telnyx.verifications.actions.verify(
          latest_verification.id,
          code: params[:token]
        )
        
        if result&.valid
          # Mark the user as verified
          @user.update(verified: true)

          # Send success SMS using Telnyx
          send_telnyx_message("You did it! Signup complete :)")
          
          flash[:notice] = "Verification successful!"
          redirect_to user_path(@user.id)
        else
          flash.now[:danger] = "Incorrect code, please try again"
          render :show_verify
        end
      else
        flash.now[:danger] = "No pending verification found. Please request a new code."
        render :show_verify
      end
    rescue StandardError => e
      Rails.logger.error("Telnyx Verify error: #{e.message}")
      Rails.logger.error(e.backtrace&.first(5)&.join("\n"))
      flash.now[:danger] = "Verification failed: #{e.message}"
      render :show_verify
    end
  end

  def resend
    @user = current_user
    
    begin
      # Initialize Telnyx client
      telnyx = Telnyx::Client.new(api_key: ENV['TELNYX_API_KEY'])
      
      # Get the profile ID
      verify_profile_id = @user.authy_id
      phone_number = "#{@user.country_code}#{@user.phone_number}"
      
      if verify_profile_id.present?
        # Resend verification code
        verification = telnyx.verifications.trigger_sms(
          phone_number: phone_number,
          verify_profile_id: verify_profile_id,
          timeout_secs: 300
        )
        
        flash[:notice] = 'Verification code re-sent'
        Rails.logger.info("Verification #{verification.id} resent")
      else
        flash[:alert] = "No verification profile found. Please sign up again."
      end
    rescue StandardError => e
      Rails.logger.error("Telnyx resend error: #{e.message}")
      Rails.logger.error(e.backtrace&.first(5)&.join("\n"))
      flash[:alert] = "Could not resend verification code: #{e.message}"
    end
    
    redirect_to verify_path
  end

  private

  def send_telnyx_message(message)
    @user = current_user
    
    begin
      # Initialize Telnyx client
      telnyx = Telnyx::Client.new(api_key: ENV['TELNYX_API_KEY'])
      
      from_number = ENV['TELNYX_PHONE_NUMBER']
      to_number = "#{@user.country_code}#{@user.phone_number}"
      
      # Send SMS using Telnyx messaging API
      result = telnyx.messages.create(
        from: from_number,
        to: to_number,
        text: message
      )
      
      Rails.logger.info("SMS sent: #{result&.id}")
    rescue StandardError => e
      Rails.logger.error("Telnyx message error: #{e.message}")
      Rails.logger.error(e.backtrace&.first(5)&.join("\n"))
    end
  end

  def user_params
    params.require(:user).permit(
      :email, :password, :name, :country_code, :phone_number
    )
  end
end
