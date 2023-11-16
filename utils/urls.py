from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('validate-email', csrf_exempt(EmailValidation.as_view()), name='utils-validate-email'),
    path('college-list', csrf_exempt(CollegeList.as_view()), name='utils-college-list'),
    path('country-list', csrf_exempt(CountryList.as_view()), name='utils-country-list'),
]