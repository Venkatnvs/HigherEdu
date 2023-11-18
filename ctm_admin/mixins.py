from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden

class CheckAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return HttpResponseForbidden("You don't have permission to access this page.")