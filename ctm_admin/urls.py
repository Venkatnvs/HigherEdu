from django.urls import path
from .views import *

urlpatterns = [
    path("", Main, name="ctm_admin-main"),
    path("all-users/", UsersListview.as_view(), name="ctm_admin-all-users"),
    path("contact-messages/", ContactUsListview.as_view(), name="ctm_admin-contact-messages"),


    path("export-excel-all-users/", UserDataExportExcel, name="ctm_admin-export-excel-all-users"),
    path("export-csv-all-users/", UserDataExportCsv, name="ctm_admin-export-csv-all-users"),
]