from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='dashboard-home' ),
    path('profile/', ProfileUpdate.as_view(), name='dashboard-profile' ),
    path('update-password/', UpdatePassword.as_view(), name='dashboard-update-password' ),
]