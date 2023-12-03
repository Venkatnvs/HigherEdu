from django.shortcuts import render
from .models import AvaliableCourses,ApplyCourse
from django.views import View
from django.http import HttpResponseNotFound
from django.contrib.auth.mixins import LoginRequiredMixin

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