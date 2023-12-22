from django.conf import settings
from applies.models import ForeignLanguage,CompetitiveCourse

def Appdata(request):
    context = {
        'site_name':settings.SITE_NAME,
        'languages_sidebar_admin':ForeignLanguage.objects.all(),
        'courses_sidebar_admin':CompetitiveCourse.objects.all()
    }
    return context