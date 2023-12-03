from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile,CustomUser
from django.http import HttpResponseNotFound,HttpResponseForbidden
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.helpers import extract_first_last_name
from django.contrib import messages
from .mixins import CheckBasicAuthMixin
from .decorators import check_basic_auth

@check_basic_auth
def Home(request):
    return render(request,"dashboard/index.html")


class ProfileUpdate(CheckBasicAuthMixin,View):
    def get(self,request):
        user = UserProfile.objects.filter(user=request.user)
        if not user.exists():
            return HttpResponseNotFound("Page Not Found")
        user = user.first()
        context = {
            'user':user,
            'preferred_college_values':user.preferred_college_list
        }
        return render(request, 'profile/view_profile.html',context)
    
    def post(self,request):
        fullname = request.POST['fullname']
        gender = request.POST['gender']
        mobile_no = request.POST['mobile_no']
        mobile_no_full = request.POST['mobile_no_full']
        usn_no = request.POST['usn_no']
        college = request.POST['college']
        graduation = request.POST['graduation']
        country = request.POST['country']
        course = request.POST['course']
        preferred_college = request.POST.getlist('preferred_college[]')
        abroad_year = request.POST['abroad_year']
        season = request.POST['season']
        fullname = fullname.strip()
        preferred_college = '\r\n'.join([college for college in preferred_college])
        if fullname == "":
            messages.error(request,"Full name cannot be Empty")
            return redirect('dashboard-profile')
        if len(mobile_no)>12:
            messages.error(request, 'Invalid Mobile Number')
            return redirect('dashboard-profile')
        first_name, last_name = extract_first_last_name(fullname)
        try:
            user = UserProfile.objects.get(user=request.user)
        except Exception as e:
            print(e)
            return HttpResponseForbidden("Not Allowed")
        user.user.first_name = first_name
        user.user.last_name = last_name
        user.gender = gender
        user.mobile_no = mobile_no_full
        user.usn = usn_no
        user.college = college
        user.graduation_year = graduation
        user.country = country
        user.abroad_year = abroad_year
        user.course  = course
        user.preferred_college = preferred_college
        user.abroad_season  = season
        user.user.save()
        user.save()
        messages.success(request,"Profile Updated Successfully")
        return redirect('dashboard-profile')
    

class UpdatePassword(CheckBasicAuthMixin,View):
    def get(self,request):
        return render(request,'profile/update_password.html')
    
    def post(self,request):
        crpassword = request.POST['crpassword']
        password = request.POST['password']
        copassword = request.POST['copassword']
        if not (password == copassword):
            messages.error(request,'Password donot match')
            return render(request,'profile/update_password.html')
        if len(password)<8:
            messages.error(request,'Password too short')
            return render(request,'profile/update_password.html')
        try:
            user = CustomUser.objects.get(email=request.user.email)
        except Exception as e:
            print(e)
            return HttpResponseForbidden("Not Allowed")
        if not user.check_password(crpassword):
            messages.error(request,'Incorrect Current Password')
            return render(request,'profile/update_password.html')
        user.set_password(password)
        user.save()
        messages.success(request,'Password updated successfully')
        return redirect('dashboard-update-password')
    
def CareerCounsellingPage(request):
    return render(request,'dashboard/services/career-counselling.html')

def ScholarshipPage(request):
    return render(request,'dashboard/services/scholarship.html')

def VisaAssistancePage(request):
    return render(request,'dashboard/services/visa-assistance.html')

def TestPreparationPage(request):
    return render(request,'dashboard/services/test-preparation.html')

def AboutPage(request):
    return render(request,'dashboard/about/index.html')

import requests
from django.http import HttpResponse,JsonResponse
import json
def Test(request):
    return render(request,'dashboard/test.html')
def Test2(request):
    return render(request,'dashboard/test2.html')

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  # This is used for simplicity. In production, use a proper CSRF protection method.
def chat_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_message = data.get('user_message', '')
        # Add your chat logic here to generate the bot's reply
        bot_reply = "You said: " + user_message
        return JsonResponse({'reply_message': bot_reply})
    else:
        return JsonResponse({'error': 'Invalid request method'})
def proxy_openstreetmap_image(request):
    url = "https://staticmap.openstreetmap.de/staticmap.php?center=40.748817,-73.985428&zoom=14&size=2048x1024&maptype=mapnik"
    response = requests.get(url)
    return HttpResponse(response.content, content_type=response.headers['Content-Type'])