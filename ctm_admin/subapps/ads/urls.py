from django.urls import path
from .views import *

urlpatterns = [
    path("get_new_refresh", get_new_ad_refresh, name="ads-refresh"),
]