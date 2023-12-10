from django import forms
from .models import ForeignLanguage, CompetitiveCourse

class ApplyLanguagesForm(forms.Form):
    LANGUAGES = ForeignLanguage.objects.all().values_list('name', 'name')

    languages = forms.ChoiceField(
        choices=LANGUAGES,
        required=False
    )

class ApplyCoursesForm(forms.Form):
    COURSES = CompetitiveCourse.objects.all().values_list('short_name', 'name')

    courses = forms.ChoiceField(
        choices=COURSES,
        required=False
    )