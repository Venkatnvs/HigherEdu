from django import template
from ctm_admin.subapps.ads.utils import GetAds

register = template.Library()

@register.filter
def GetAd_size(value, arg):
    url,forward,H,W = GetAds(arg)
    html_send = f"""<img style="max-width:{W}px;max-height:{H}px;cursor: pointer;" onclick="window.open('{forward}', '_blank')" class="img_fluid" src="{url}" alt="ad_{arg}">"""
    return html_send