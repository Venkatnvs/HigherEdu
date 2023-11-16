from django.shortcuts import render
from django.views import View
from django.contrib import messages

class Registration(View):
    def get(self, request):
        # messages.error(request,"Hello")
        
        return render(request, 'accounts/register.html')

    def post(self, request):
        pass