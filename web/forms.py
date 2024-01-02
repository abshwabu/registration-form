from django import forms

class RegistrationStep1Form(forms.Form):
    usernames = forms.CharField(max_length=100)
    email= forms.EmailField()

class RegistrationStep2Form(forms.Form):
    password1 = forms.CharField(widget= forms.PasswordInput)
    password2 = forms.CharField(widget= forms.PasswordInput)