from django.urls import path,include
from .views import *
from .contacts_views import *

urlpatterns = [
    path("", Main, name="ctm_admin-main"),
    path("all-users/", UsersListview.as_view(), name="ctm_admin-all-users"),

    # Contact Messages
    path("contactus/", ContactUsListview.as_view(), name="ctm_admin-contactus_list"),
    path('contactus/<int:pk>/', ContactUsDetailView.as_view(), name='ctm_admin-contactus_detail'),
    path('contactus/<int:pk>/edit/', ContactUsUpdateView.as_view(), name='ctm_admin-contactus_edit'),
    path('contactus/<int:pk>/delete/', ContactUsDeleteView.as_view(), name='ctm_admin-contactus_delete'),

    # Data Export
    path("export-excel-all-users/", UserDataExportExcel, name="ctm_admin-export-excel-all-users"),
    path("export-csv-all-users/", UserDataExportCsv, name="ctm_admin-export-csv-all-users"),

    # ADS System
    path("ads/",include('ctm_admin.subapps.ads.urls')),
]