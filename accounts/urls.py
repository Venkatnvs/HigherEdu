from django.urls import path, include
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', Registration.as_view(), name='accounts-register' ),
]