from django.contrib import admin
from .models import AvaliableCourses,ApplyCourse,ForeignLanguage,ForeignLanguageApplied,CompetitiveCourse,CompetitiveCourseApplied

admin.site.register(AvaliableCourses)
admin.site.register(ApplyCourse)
admin.site.register(ForeignLanguage)
admin.site.register(ForeignLanguageApplied)
admin.site.register(CompetitiveCourse)
admin.site.register(CompetitiveCourseApplied)