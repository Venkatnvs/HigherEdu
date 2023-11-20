from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages

class CheckBasicAuthMixin(LoginRequiredMixin,UserPassesTestMixin):
    def test_func(self):
        if self.request.user.is_socialaccount:
            return self.request.user.is_completed
        return self.request.user.is_active

    def handle_no_permission(self,request):
        messages.warning(request,'Complete your Account Setup')
        return redirect("accounts-complete-social")