from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import AvaliableCourses,ApplyCourse
from django.views import View
from django.http import HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ApplyLanguagesForm,ApplyCoursesForm
from .models import ForeignLanguageApplied,ForeignLanguage,CompetitiveCourse,CompetitiveCourseApplied
from django.contrib import messages
import os
from django.conf import settings
import json

def CountryByApply(request):
    crs = AvaliableCourses.objects.filter(is_active=True)
    context = {
        'data':crs
    }
    return render(request,'applies/bycnt/index.html',context)

class ApplyForCourse(LoginRequiredMixin,View):
    file_path = os.path.join(settings.BASE_DIR,'datasets/countries.json')

    def check_url_id(self,id):
        av = get_object_or_404(AvaliableCourses,id=id)
        return av

    def get_cnt(self,c):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        country = ""
        for i in data:
            if c.lower() == i['code'].lower():
                country = i['name']
        return country
    
    def dispatch(self, request, *args, **kwargs):
        av = self.check_url_id(self.kwargs.get("id", None))
        if not request.user.is_authenticated:
            messages.info(request, "You need to be logged in to apply for this course.")
            return redirect('accounts-login')
        if av:
            acc = ApplyCourse.objects.filter(user=request.user, course=av)
            if acc.exists():
                messages.info(request, "Course Already Applied.")
                return redirect('applies-courses')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id):
        av = self.check_url_id(self.kwargs.get("id", None))
        context = {
            "av_course":av,
            "cnt_a":self.get_cnt(av.country_code)
        }
        return render(request, 'applies/bycnt/apply_form.html',context)
    
    def post(self,request,id):
        course = request.POST['course']
        if not course:
            messages.error(request,"Course cannot be Empty")
            return redirect('applies-courses-apply',id=id)
        preferred_college = request.POST.getlist('preferred_college[]')
        if len(preferred_college)<=0:
            messages.error(request,"Preferred colleges cannot be Empty")
            return redirect('applies-courses-apply',id=id)
        abroad_year = request.POST['abroad_year']
        if not abroad_year:
            messages.error(request,"Year Of Study cannot be Empty")
            return redirect('applies-courses-apply',id=id)
        season = request.POST['season']
        preferred_college_list = '\r\n'.join([college for college in preferred_college])
        av = self.check_url_id(id)
        ac = ApplyCourse.objects.create(
            user = request.user,
            course = av,
            preferred_college = preferred_college_list,
            course_type = course,
            abroad_year = abroad_year,
            abroad_season = season,
            is_active = True
        )
        av.save()
        messages.success(request,f"Applied to Course in {av.country}.")
        return redirect('applies-courses')
    
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