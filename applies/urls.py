from django.urls import path
from .views import *

urlpatterns = [
    path("courses", CountryByApply, name="applies-courses"),
    path("courses/<int:id>/apply", ApplyForCourse.as_view(), name="applies-courses-apply"),
    path('apply/foreign-languages/', ApplyForeignLanguagesView.as_view(), name='applies-foreign-languages'),
    path('apply/courses/', ApplyCoursesView.as_view(), name='applies-apply_courses'),
]