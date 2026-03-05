class VacationPropertiesController < ApplicationController
  before_action :authenticate_user, except: [:index]
  before_action :set_vacation_property_and_user, only: [:show, :edit, :update, :destroy]

  # GET /vacation_properties
  # GET /vacation_properties.json
  def index
    @vacation_properties = VacationProperty.all
  end

  # GET /vacation_properties/1
  # GET /vacation_properties/1.json
  def show
    @reservation = Reservation.new
    begin
      @current_reservation = Reservation.where(
        vacation_property_id: @vacation_property.id, 
        guest_phone: @user.phone_number,
        status: 1)
      .first 
    rescue Exception => e
      puts "e.message"
    end
  end

  # GET /vacation_properties/new
  def new
    @vacation_property = VacationProperty.new
  end

  # GET /vacation_properties/1/edit
  def edit
  end

  def create
    @user = current_user
    @vacation_property = @user.vacation_properties.create(vacation_property_params)

    respond_to do |format|
      if @vacation_property.save
        format.html { redirect_to @vacation_property, notice: 'Vacation property was successfully created.' }
        format.json { render :show, status: :created, location: @vacation_property }
      else
        format.html { render :new }
        format.json { render json: @vacation_property.errors, status: :unprocessable_entity }
      end
    end
  end

  def update
    respond_to do |format|
      if @vacation_property.update(vacation_property_params)
        format.html { redirect_to @vacation_property, notice: 'Vacation property was successfully updated.' }
        format.json { render :show, status: :ok, location: @vacation_property }
      else
        format.html { render :edit }
        format.json { render json: @vacation_property.errors, status: :unprocessable_entity }
      end
    end
  end

  def destroy
    @vacation_property.destroy
    respond_to do |format|
      format.html { redirect_to vacation_properties_url, notice: 'Vacation property was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_vacation_property_and_user
      @user = current_user
      @vacation_property = VacationProperty.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def vacation_property_params
      params.require(:vacation_property).permit(:description, :image_url)
    end
end
