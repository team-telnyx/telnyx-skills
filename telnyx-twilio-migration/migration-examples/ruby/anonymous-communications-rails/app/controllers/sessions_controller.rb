class SessionsController < ApplicationController
  before_action :authenticate_user, :except => [:login, :login_attempt]
  before_action :save_login_state, :only => [:login, :login_attempt]

  def login
    #Login Form
  end

  def login_attempt
    user = User.find_by_email(params[:email])
    if user && user.authenticate(params[:login_password])
      session[:user_id] = user.id
      flash[:notice] = "Welcome again, you logged in as #{user.email}"
      redirect_to home_path

    else
      flash[:notice] = "Invalid Username or Password"
      render "login"
    end
  end

  def logout
    session[:user_id] = nil
    redirect_to :action => 'login'
  end

end