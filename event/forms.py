from django import forms
from models import Event

class ContactForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('date_update',)