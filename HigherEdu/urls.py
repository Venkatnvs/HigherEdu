from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView

fav_icon = RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('utils/', include('utils.urls')),
    re_path(r'^favicon\.ico$', fav_icon),
]
if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)