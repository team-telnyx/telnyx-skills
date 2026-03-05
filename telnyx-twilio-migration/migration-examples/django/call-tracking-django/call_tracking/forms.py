from django import forms
from phonenumber_field.formfields import PhoneNumberField


class AreaCodeForm(forms.Form):
    """Form for specifying the area code when searching for available numbers"""
    area_code = forms.CharField(min_length=3, max_length=3, required=False)


class PurchaseNumberForm(forms.Form):
    """Form for purchasing a number from the Twilio API"""
    phone_number = PhoneNumberField()
