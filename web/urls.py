from .views import RegistrationWizardView

from django.urls import path

urlpatterns =[
    path('register/',RegistrationWizardView.as_view(),name='registration_wizard'),
]