from django.http import JsonResponse
from django.template.loader import render_to_string
from ctm_admin.subapps.ads.utils import GetAds
from django.views import View

def get_new_ad_refresh(request):
    size = request.GET.get('size', '300x200')
    url, forward, H, W = GetAds(size)
    html_send = render_to_string('ads_snippets/ads_refresh.html', {'url': url, 'forward': forward, 'H': H, 'W': W, 'size':size})
    return JsonResponse({'new_ad_html': html_send})

class AdminADS(View):
    pass