from django.shortcuts import render
from .models import AvaliableCourses

def CountryByApply(request):
    crs = AvaliableCourses.objects.filter(is_active=True)
    context = {
        'data':crs
    }
    return render(request,'applies/bycnt/index.html',context)