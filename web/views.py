from formtools.wizard.views import SessionWizardView
from .forms import RegistrationStep1Form, RegistrationStep2Form
from django.shortcuts import render
from django.contrib.auth import get_user_model,login
class RegistrationWizardView(SessionWizardView):
    form_list = [RegistrationStep1Form, RegistrationStep2Form]
    template_name = 'registration_wizard.html'

    def done(self, form_list, **kwargs):
        username = form_list[0].cleaned_data['username']
        email = form_list[0].cleaned_data['email']
        password = form_list[1].cleaned_data['password1']

        User = get_user_model()
        user = User.objects.create_user(username=username, email=email, password=password)
        login(self.request,user)
        return render(self.request, 'registration_done.html', {})