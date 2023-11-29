from django.urls import path
from .views import *

urlpatterns = [
    path("courses", CountryByApply, name="applies-courses"),
]