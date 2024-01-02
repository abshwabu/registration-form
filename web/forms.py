from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegistrationStep1Form(UserCreationForm):
    email = forms.EmailField(label='Email')

class RegistrationStep2Form(forms.Form):
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
