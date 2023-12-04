from django import template
from ctm_admin.subapps.ads.utils import GetAds

register = template.Library()

@register.filter
def GetAd_size(value, arg):
    url,forward,H,W = GetAds(arg)
    html_send = f"""<div style="position: relative;width: auto;display: inline-block;box-sizing: border-box;">
<span style="position:absolute;bottom:0;padding: 2px; background-color: #000000ba; color: #fff; z-index: 9;border-top-right-radius: 3px;">ad</span>
<img style="max-width:100%!important;height: 100%;width:{W}px;max-height:{H}px;cursor: pointer;" onclick="window.open('{forward}', '_blank')" class="img_fluid" src="{url}" alt="ad_{arg}">
</div>"""
    return html_send