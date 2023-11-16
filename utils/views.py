from django.shortcuts import render
from django.views import View
import json
from validate_email import validate_email
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import os
from django.conf import settings

User = get_user_model()

class EmailValidation(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error':'Email is invalid'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error':'Sorry email is already registered'})
        return JsonResponse({'email_valid':True})

class CollegeList(View):
    file_path = os.path.join(settings.BASE_DIR,'datasets/colleges.json')
    
    def get(self,request):
        term = request.GET.get('q', '')
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        filtered_colleges = [entry['college'] for entry in data if term.lower() in entry['college'].lower()]
        return JsonResponse(filtered_colleges, safe=False)

class CountryList(View):
    file_path = os.path.join(settings.BASE_DIR,'datasets/countries.json')
    
    def get(self,request):
        term = request.GET.get('q', '')
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        filtered_colleges = [entry['name'] for entry in data if term.lower() in entry['name'].lower()]
        return JsonResponse(filtered_colleges, safe=False)