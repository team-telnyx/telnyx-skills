from airtng_flask.models import (
    app_db,
    telnyx_api_key,
    telnyx_phone_number,
    telnyx_messaging_profile_id,
    telnyx_connection_id,
)
from flask import render_template
import telnyx

DB = app_db()


class Reservation(DB.Model):
    __tablename__ = "reservations"

    id = DB.Column(DB.Integer, primary_key=True)
    message = DB.Column(DB.String, nullable=False)
    status = DB.Column(
        DB.Enum('pending', 'confirmed', 'rejected', name='reservation_status_enum'),
        default='pending',
    )
    anonymous_phone_number = DB.Column(DB.String, nullable=True)
    guest_id = DB.Column(DB.Integer, DB.ForeignKey('users.id'))
    vacation_property_id = DB.Column(
        DB.Integer, DB.ForeignKey('vacation_properties.id')
    )
    guest = DB.relationship("User", back_populates="reservations")
    vacation_property = DB.relationship(
        "VacationProperty", back_populates="reservations"
    )

    def __init__(self, message, vacation_property, guest):
        self.message = message
        self.guest = guest
        self.vacation_property = vacation_property
        self.status = 'pending'

    def confirm(self):
        self.status = 'confirmed'

    def reject(self):
        self.status = 'rejected'

    def __repr__(self):
        return '<Reservation {0}>'.format(self.id)

    def notify_host(self):
        self._send_message(
            self.vacation_property.host.phone_number,
            render_template(
                'messages/sms_host.txt',
                name=self.guest.name,
                description=self.vacation_property.description,
                message=self.message,
            ),
        )

    def notify_guest(self):
        self._send_message(
            self.guest.phone_number,
            render_template(
                'messages/sms_guest.txt',
                description=self.vacation_property.description,
                status=self.status,
            ),
        )

    def buy_number(self, area_code):
        """
        Purchase a phone number for masked communication.
        Uses Telnyx Number Pool API instead of Twilio available_phone_numbers.
        """
        client = self._get_telnyx_client()
        
        # Search for available phone numbers by area code
        try:
            available_numbers = client.available_phone_numbers.list(
                filter={"locality": "United States", "area_code": area_code}
            )
            
            if available_numbers.data:
                number = self._purchase_number(client, available_numbers.data[0].phone_number)
                self.anonymous_phone_number = number
                return number
            else:
                # Fallback: search without area code constraint
                available_numbers = client.available_phone_numbers.list(
                    filter={"locality": "United States"}
                )
                
                if available_numbers.data:
                    number = self._purchase_number(client, available_numbers.data[0].phone_number)
                    self.anonymous_phone_number = number
                    return number
        except Exception as e:
            print(f"Error buying number: {e}")
            
        return None

    def _purchase_number(self, client, phone_number):
        """
        Purchase a phone number and configure it for messaging and voice.
        """
        try:
            # Create a number order
            number_order = client.number_orders.create(
                phone_numbers=[{"phone_number": phone_number}],
                connection_id=telnyx_connection_id(),
                messaging_profile_id=telnyx_messaging_profile_id()
            )
            
            return phone_number
        except Exception as e:
            print(f"Error purchasing number: {e}")
            raise

    def _get_telnyx_client(self):
        """Initialize Telnyx client with API key."""
        telnyx.api_key = telnyx_api_key()
        return telnyx

    def _send_message(self, to, message):
        """Send SMS using Telnyx Messaging API."""
        client = self._get_telnyx_client()
        
        try:
            response = client.messages.send(
                from_=telnyx_phone_number(),
                to=to,
                text=message,
                messaging_profile_id=telnyx_messaging_profile_id()
            )
            return response
        except Exception as e:
            print(f"Error sending message: {e}")
            raise
