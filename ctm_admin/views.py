from django.shortcuts import render,HttpResponse
from .mixins import CheckAdminMixin
from .decorators import check_admin_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from accounts.models import UserProfile,CustomUser
import xlwt
import csv
import datetime
from django.db.models import F,Value, CharField
from django.db.models.functions import Cast, Coalesce, Concat
from .dashboard import chart_view
import json
from django.core.serializers.json import DjangoJSONEncoder
from utils.models import ContactUs

@check_admin_required
def Main(request):
    users = CustomUser.objects.filter(is_superuser=False)
    user_count = users.count()
    contact_msg_count = ContactUs.objects.filter(is_replyed=False).count()
    a,b= chart_view()
    context = {
        "user_count":user_count,
        "contact_msg_count":contact_msg_count,
        "graphs_1":json.dumps(a,cls=DjangoJSONEncoder),
        "graphs_2":json.dumps(b,cls=DjangoJSONEncoder),
    }
    return render(request,'ctm_admin/index.html',context)

class UsersListview(CheckAdminMixin,ListView):
    model = UserProfile
    template_name = 'ctm_admin/allusers_list.html'

    def get_queryset(self):
        return UserProfile.objects.filter(user__is_superuser=False).order_by('created_at')

@check_admin_required
def UserDataExportExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserData'+str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('UserInfo')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Email','Full Name','Gender','Mobile No.','Verification Status','Usn','College','Graduation Year','Abroad Country','Abroad Course','Abroad Preferred Country','Abroad Year','Abroad Season','Created at']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style =  xlwt.XFStyle()
    rows = UserProfile.objects.filter(user__is_superuser=False).annotate(
        first_name=F('user__first_name'),
        last_name=F('user__last_name'),
        full_name=Coalesce(Concat(Cast('first_name', CharField()), Value(' '), Cast('last_name', CharField())), 'first_name')
        ).values_list(
            'user__email',
            'full_name',
            'gender',
            'mobile_no',
            'user__is_active',
            'usn','college',
            'graduation_year','country',
            'course','preferred_college',
            'abroad_year','abroad_season',
            'created_at')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

@check_admin_required
def UserDataExportCsv(request):
    response = HttpResponse(content_type='text/csv')
    file_name = f'UserData{str(datetime.datetime.now())}.csv'
    response['Content-Disposition'] = 'attachment; filename='+file_name
    writer = csv.writer(response)
    writer.writerow(['Email','Full Name','Gender','Mobile No.','Verification Status','Usn','College','Graduation Year','Abroad Country','Abroad Course','Abroad Preferred Country','Abroad Year','Abroad Season','Created at'])

    rows = UserProfile.objects.filter(user__is_superuser=False).annotate(
        first_name=F('user__first_name'),
        last_name=F('user__last_name'),
        full_name=Coalesce(Concat(Cast('first_name', CharField()), Value(' '), Cast('last_name', CharField())), 'first_name')
        ).values_list(
            'user__email',
            'full_name',
            'gender',
            'mobile_no',
            'user__is_active',
            'usn','college',
            'graduation_year','country',
            'course','preferred_college',
            'abroad_year','abroad_season',
            'created_at')

    for row in rows:
        writer.writerow(row)

    return response