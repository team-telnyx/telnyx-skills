class ApplicationController < ActionController::Base
  # Prevent CSRF attacks by raising an exception.
  # For APIs, you may want to use :null_session instead.
  protect_from_forgery with: :null_session

  def current_user
    User.find_by(id: session[:user_id])
  end
  helper_method :current_user

  def signed_in?
    current_user.present?
  end
  helper_method :signed_in?

  protected

  def authenticate_user
    unless session[:user_id]
      redirect_to(controller: 'sessions', action: 'login')
      flash[:notice] = "You must be logged in to view that page."
      return false
    else
      @user = User.find session[:user_id]
      return true
    end
  end

  def save_login_state
    if session[:user_id]
      redirect_to home_path
      return false
    else
      return true
    end
  end

end
