from django.urls import path
from .views import *

urlpatterns = [
    # Foreign Languages Applied
    path('foreign-languages-list/', AdminForeignLangList.as_view(), name='ctm_admin-foreign-languages-list'),
    path('foreign-languages-list/<slug:language_slug>/', AdminForeignLangListSpecific.as_view(), name='ctm_admin-foreign-languages-list-specific'),
    path('competitive-courses-list/', AdminCompetitiveCoursesList.as_view(), name='ctm_admin-competitive-courses-list'),
    path('competitive-courses-list/<slug:course_slug>/', AdminCompetitiveCoursesListSpecific.as_view(), name='ctm_admin-competitive-courses-list-specific'),

    # Data Export
    path("export-excel-all-users-lang/", ForeignLangUserDataExportExcel, name="ctm_admin-all-foreign-languages-export-excel"),
    path("export-csv-all-users-lang/", ForeignLangUserDataExportCsv, name="ctm_admin-all-foreign-languages-export-csv"),

    path("export-excel-all-users-courses/", CompetitiveCoursesUserDataExportExcel, name="ctm_admin-all-competitive-courses-export-excel"),
    path("export-csv-all-users-courses/", CompetitiveCoursesUserDataExportCsv, name="ctm_admin-all-competitive-courses-export-csv"),
]