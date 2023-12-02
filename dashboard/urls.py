from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home, name='dashboard-home' ),
    path('profile/', ProfileUpdate.as_view(), name='dashboard-profile' ),
    path('update-password/', UpdatePassword.as_view(), name='dashboard-update-password' ),

    # About Page
    path('about/',AboutPage,name="dashboard-about"),

    # Services Pages
    path('services/career-counselling/',CareerCounsellingPage,name="services-career-counselling"),
    path('services/scholarships/',ScholarshipPage,name="services-scholarships"),
    path('services/visa-assistance/',VisaAssistancePage,name="services-visa-assistance"),
    path('services/test-preparation/',TestPreparationPage,name="services-test-preparation"),
]