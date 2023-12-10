from django import forms
# from .models import ForeignLanguage, CompetitiveCourse

class ApplyLanguagesForm(forms.Form):
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