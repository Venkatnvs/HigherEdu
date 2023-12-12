from django import forms
from .models import ForeignLanguage, CompetitiveCourse

class ApplyLanguagesForm(forms.Form):
    try:
        LANGUAGES = ForeignLanguage.objects.all().values_list('name', 'name')
    except Exception as e:
        print(e)
        LANGUAGES = [
            ('german', 'German'),
            ('french', 'French'),
            ('japanese', 'Japanese'),
            ('spanish', 'Spanish'),
        ]

    languages = forms.ChoiceField(
        choices=LANGUAGES,
        required=False
    )

class ApplyCoursesForm(forms.Form):
    try:
        COURSES = CompetitiveCourse.objects.all().values_list('short_name', 'name')
    except Exception as e:
        print(e)
        COURSES = [
            ('gre', 'GRE / GMAT / CAT coaching'),
            ('gate', 'GATE Coaching'),
            ('upsc', 'Civil services (UPSC) IAS/IPS/IFS Coaching'),
            ('ielts', 'IELTS (the International English Language Testing System)'),
        ]

    courses = forms.ChoiceField(
        choices=COURSES,
        required=False
    )