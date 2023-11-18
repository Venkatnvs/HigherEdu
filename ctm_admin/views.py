from django.shortcuts import render,HttpResponse
from .mixins import CheckAdminMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from accounts.models import UserProfile,CustomUser
import xlwt
import csv
import datetime
from django.db.models import F,Value, CharField
from django.db.models.functions import Cast, Coalesce, Concat

def Main(request):
    users = CustomUser.objects.filter(is_superuser=False)
    user_count = users.count()
    context = {
        "user_count":user_count,
    }
    return render(request,'ctm_admin/index.html',context)


class UsersListview(ListView):
    model = UserProfile
    template_name = 'ctm_admin/allusers_list.html'
    paginate_by = 20

    def get_queryset(self):
        return UserProfile.objects.filter(user__is_superuser=False).order_by('created_at')


def UserDataExportExcel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserData'+str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('UserInfo')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Email','Full Name','Gender','Mobile No.','Verification Status','Usn','College','Graduation Year','Abroad Country','Abroad Course','Abroad Year','Abroad Season','Created at']
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
            'course','abroad_year','abroad_season',
            'created_at')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

def UserDataExportCsv(request):
    response = HttpResponse(content_type='text/csv')
    file_name = f'UserData{str(datetime.datetime.now())}.csv'
    response['Content-Disposition'] = 'attachment; filename='+file_name
    writer = csv.writer(response)
    writer.writerow(['Email','Full Name','Gender','Mobile No.','Verification Status','Usn','College','Graduation Year','Abroad Country','Abroad Course','Abroad Year','Abroad Season','Created at'])

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
            'course','abroad_year','abroad_season',
            'created_at')

    for row in rows:
        writer.writerow(row)

    return response