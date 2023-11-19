from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

def check_admin(user):
    return user.is_superuser

check_admin_decorator = user_passes_test(check_admin, login_url=None)

def check_admin_required(view_func):
    decorated_view_func = check_admin_decorator(view_func)
    
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts-login')
        return decorated_view_func(request, *args, **kwargs)

    return wrapper
