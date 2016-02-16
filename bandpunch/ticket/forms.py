from django import forms
from django.forms import models, extras
from django.core.validators import validate_email
from django.contrib.auth.models import User

from datetime import datetime

from ticket.models import CardChoices, Purchase, UserAccount, alphanumeric_RE
from ticket.fields import CreditCardField, ExpiryDateField, VerificationValueField

class ContactForm(forms.Form):
    """Form for the contact page containing relevant fields and appropriate attributes."""
    name = forms.CharField(required=True, max_length=100, label='Name')
    email = forms.EmailField(required=True, label='E-mail Address', validators=[validate_email])
    subject = forms.CharField(required=True, label='Subject')
    query = forms.CharField(required=True, widget=forms.Textarea)

class PurchaseForm(forms.ModelForm):
	# Custom fields overwrite the ones in the Purchase model
	payment_type = forms.ModelChoiceField(queryset=CardChoices.objects.all())
	card_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Card Holder's Name"}))
	card_number = CreditCardField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Credit / Debit card number'}))
	security_code = VerificationValueField(required=True)
	expiry_date = ExpiryDateField(required=True)
	DELIVERY_CHOICES = (
		(True, 'Collect from Venue'),
		(False, 'Print Ticket'),
	)
	delivery_option = forms.ChoiceField(choices=DELIVERY_CHOICES, widget=forms.RadioSelect())
	email_receipt = forms.BooleanField(required=False, label='Tick this box to receive an e-mail receipt')
	email = forms.EmailField(required=False, label='E-mail address', validators=[validate_email])

	class Meta:
		model = Purchase
		fields = ("payment_type", "card_name", "card_number", "security_code", "expiry_date", "delivery_option", "email_receipt", "email")

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ("username", "email", "password")

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserAccount
		fields = ("name", "address", "phone_number")