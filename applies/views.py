from django.shortcuts import render,redirect
from .models import AvaliableCourses,ApplyCourse
from django.views import View
from django.http import HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ApplyLanguagesForm,ApplyCoursesForm
from .models import ForeignLanguageApplied,ForeignLanguage,CompetitiveCourse,CompetitiveCourseApplied
from django.contrib import messages

def CountryByApply(request):
    crs = AvaliableCourses.objects.filter(is_active=True)
    context = {
        'data':crs
    }
    return render(request,'applies/bycnt/index.html',context)

class ApplyForCourse(LoginRequiredMixin,View):

    def get(self,request,id):
        av = AvaliableCourses.objects.filter(id=id)
        if not av.exists():
            return HttpResponseNotFound("Course not found. Try aganin!")
        av = av.first()
        context = {
            "url_id":av.id
        }
        return render(request, 'applies/bycnt/apply_form.html',context)
    
class ApplyForeignLanguagesView(LoginRequiredMixin,View):
    form = ApplyLanguagesForm()
    def get(self,request,*args, **kwargs):
        return render(request, 'applies/apply_languages.html', {'form': self.form})
    
    def post(self,request,*args, **kwargs):
        form = ApplyLanguagesForm(request.POST)
        if form.is_valid():
            user = request.user
            language_name = form.cleaned_data['languages']
            existing_languages = ForeignLanguageApplied.objects.filter(user=user, languages__name=language_name)
            if existing_languages.exists():
                return render(request, 'applies/apply_languages.html', {'form': form, 'error_message': 'You have already applied to selected languages.'})
            language_application,c = ForeignLanguageApplied.objects.get_or_create(user=user)
            language = ForeignLanguage.objects.filter(name=language_name)
            if language.exists():
                language_application.languages.add(language.first())
            else:
                return render(request, 'applies/apply_languages.html', {'form': form, 'error_message': 'Some thing went wrong!'})
            messages.success(request,'Form submited, we will contact you soon.')
            return redirect('dashboard-home')

        return render(request, 'applies/apply_languages.html', {'form': form, 'error_message': 'Some thing went wrong!'})

class ApplyCoursesView(View):
    form = ApplyCoursesForm()
    
    def get(self,request,*args, **kwargs):
        return render(request, 'applies/apply_courses.html', {'form': self.form})
    
    def post(self,request,*args, **kwargs):
        form = ApplyCoursesForm(request.POST)
        if form.is_valid():
            user = request.user
            courses_name = form.cleaned_data['courses']
            existing_languages = CompetitiveCourseApplied.objects.filter(user=user, course__short_name=courses_name)
            if existing_languages.exists():
                return render(request, 'applies/apply_courses.html', {'form': form, 'error_message': 'You have already applied to selected Course.'})
            course_application,c = CompetitiveCourseApplied.objects.get_or_create(user=user)
            coures = CompetitiveCourse.objects.filter(short_name=courses_name)
            if coures.exists():
                course_application.course.add(coures.first())
            else:
                return render(request, 'applies/apply_courses.html', {'form': form, 'error_message': 'Some thing went wrong!1'})
            messages.success(request,'Form submited, we will contact you soon.')
            return redirect('dashboard-home')
        return render(request, 'applies/apply_courses.html', {'form': form, 'error_message': 'Some thing went wrong!'})