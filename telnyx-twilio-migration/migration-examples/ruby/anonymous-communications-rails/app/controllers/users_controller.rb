class UsersController < ApplicationController
  def new
    @user = User.new
  end

  def show
    @user = current_user
  end

  def create
    @user = User.create(user_params)

    if @user.valid?
      # Save the user_id to the session object
      session[:user_id] = @user.id
      redirect_to home_path
    else
      render :new
      flash.now[:danger] = @user.errors.full_messages
    end
  end

  private

  def user_params
    params.require(:user).permit(
      :email, :password, :name, :country_code, :area_code, :phone_number
    )
  end

end
