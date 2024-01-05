from django.urls import path
from .views import RegistrationWizardView,home
from django.views.generic import TemplateView

urlpatterns = [
    path('',home, name='home'),
    path('register/', RegistrationWizardView.as_view(), name='registration_wizard'),
    path('register/success/', TemplateView.as_view(template_name='success.html'), name='registration_success'),
    # Add other URLs as needed
]
