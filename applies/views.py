from django.shortcuts import render

def CountryByApply(request):
    return render(request,'applies/bycnt/index.html')