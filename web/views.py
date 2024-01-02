from django.shortcuts import render, redirect
from formtools.wizard.views import SessionWizardView
from .forms import RegistrationStep1Form, RegistrationStep2Form

class RegistrationWizardView(SessionWizardView):
    template_name = 'registration_wizard.html'
    form_list = [RegistrationStep1Form, RegistrationStep2Form]

    def done(self, form_list, **kwargs):
        # Combine data from all steps
        registration_data = {}
        for form in form_list:
            registration_data.update(form.cleaned_data)

        # Perform registration logic here (e.g., create user)

        return redirect('registration_success')
