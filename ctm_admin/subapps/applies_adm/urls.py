from django.urls import path
from .views import *

urlpatterns = [
    # Foreign Languages Applied
    path('foreign-languages-list/', AdminForeignLangList.as_view(), name='ctm_admin-foreign-languages-list'),
    path('competitive-courses-list/', AdminCompetitiveCoursesList.as_view(), name='ctm_admin-competitive-courses-list'),

    # Data Export
    path("export-excel-all-users-lang/", ForeignLangUserDataExportExcel, name="ctm_admin-all-foreign-languages-export-excel"),
    path("export-csv-all-users-lang/", ForeignLangUserDataExportCsv, name="ctm_admin-all-foreign-languages-export-csv"),

    path("export-excel-all-users-courses/", CompetitiveCoursesUserDataExportExcel, name="ctm_admin-all-competitive-courses-export-excel"),
    path("export-csv-all-users-courses/", CompetitiveCoursesUserDataExportCsv, name="ctm_admin-all-competitive-courses-export-csv"),
]