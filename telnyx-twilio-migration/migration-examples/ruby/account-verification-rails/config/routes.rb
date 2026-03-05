Rails.application.routes.draw do

  get "users/verify", to: 'users#show_verify', as: 'verify'
  post "users/verify"
  post "users/resend"

  # Create users
  resources :users, only: [:new, :create, :show]

  # Home page
  root 'main#index'

end