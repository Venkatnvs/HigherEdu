from django.shortcuts import render,HttpResponse
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,UpdateView,DetailView,DeleteView,CreateView
from ctm_admin.mixins import CheckAdminMixin
from applies.models import ForeignLanguageApplied,CompetitiveCourseApplied,ForeignLanguage,CompetitiveCourse
import xlwt
import csv
import datetime
from django.db.models import F,Value, CharField
from django.db.models.functions import Cast, Coalesce, Concat
from ctm_admin.decorators import check_admin_required
from django.db.models import Q

class AdminForeignLangList(CheckAdminMixin,ListView):
    model = ForeignLanguageApplied
    context_object_name = 'languages'
    template_name = 'ctm_admin/applies/foreign_lang/lang_listview.html'
    model_permissions = {
        'applies': ['view_foreignlanguageapplied']
    }

    def get_queryset(self):
        filter_val = self.request.GET.get('filter','')
        if filter_val != "":
            fl_app = ForeignLanguageApplied.objects.filter(Q(languages__name__contains=filter_val)).distinct()
        else:
            fl_app = ForeignLanguageApplied.objects.all()
        return fl_app

    def get_context_data(self, **kwargs):
        context = super(AdminForeignLangList, self).get_context_data(**kwargs)
        context['filter']=self.request.GET.get('filter','')
        context['filter_av']=ForeignLanguage.objects.all()
        return context

class AdminCompetitiveCoursesList(CheckAdminMixin,ListView):
    model = CompetitiveCourseApplied
    context_object_name = 'courses'
    template_name = 'ctm_admin/applies/competitive_course/all_applies_list.html'
    model_permissions = {
        'applies': ['view_competitivecourseapplied']
    }

    def get_queryset(self):
        filter_val = self.request.GET.get('filter','')
        if filter_val != "":
            cc_app = CompetitiveCourseApplied.objects.filter(Q(course__name__contains=filter_val)).distinct()
        else:
            cc_app = CompetitiveCourseApplied.objects.all()
        return cc_app

    def get_context_data(self, **kwargs):
        context = super(AdminCompetitiveCoursesList, self).get_context_data(**kwargs)
        context['filter']=self.request.GET.get('filter','')
        context['filter_av']=CompetitiveCourse.objects.all()
        return context

# Export Data Users

@check_admin_required
def ForeignLangUserDataExportExcel(request):
    filter_val = request.GET.get('filter','')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserData'+str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('UserInfo')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Email','Full Name','Gender','Mobile No.','Verification Status','Applied List','Created at']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style =  xlwt.XFStyle()
    rows = ForeignLanguageApplied.objects.filter(user__is_superuser=False,languages__name__contains=filter_val).annotate(
        first_name=F('user__first_name'),
        last_name=F('user__last_name'),
        full_name=Coalesce(Concat(Cast('first_name', CharField()), Value(' '), Cast('last_name', CharField())), 'first_name')
        ).values_list(
            'user__email',
            'full_name',
            'user__userprofile__gender',
            'user__userprofile__mobile_no',
            'user__is_active',
            'languages__name',
            'user__date_joined').distinct()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

@check_admin_required
def ForeignLangUserDataExportCsv(request):
    filter_val = request.GET.get('filter','')
    response = HttpResponse(content_type='text/csv')
    file_name = f'UserData{str(datetime.datetime.now())}.csv'
    response['Content-Disposition'] = 'attachment; filename='+file_name
    writer = csv.writer(response)
    writer.writerow(['Email','Full Name','Gender','Mobile No.','Verification Status','Applied List','Created at'])

    rows = ForeignLanguageApplied.objects.filter(user__is_superuser=False,languages__name__contains=filter_val).annotate(
        first_name=F('user__first_name'),
        last_name=F('user__last_name'),
        full_name=Coalesce(Concat(Cast('first_name', CharField()), Value(' '), Cast('last_name', CharField())), 'first_name')
        ).values_list(
            'user__email',
            'full_name',
            'user__userprofile__gender',
            'user__userprofile__mobile_no',
            'user__is_active',
            'languages__name',
            'user__date_joined').distinct()

    for row in rows:
        writer.writerow(row)

    return response

# Export Data Users

@check_admin_required
def CompetitiveCoursesUserDataExportExcel(request):
    filter_val = request.GET.get('filter','')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=UserData'+str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('UserAppliedCourses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Email','Full Name','Gender','Mobile No.','Verification Status','Applied List','Created at']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style =  xlwt.XFStyle()
    rows = CompetitiveCourseApplied.objects.filter(user__is_superuser=False,course__name__contains=filter_val).annotate(
        first_name=F('user__first_name'),
        last_name=F('user__last_name'),
        full_name=Coalesce(Concat(Cast('first_name', CharField()), Value(' '), Cast('last_name', CharField())), 'first_name')
        ).values_list(
            'user__email',
            'full_name',
            'user__userprofile__gender',
            'user__userprofile__mobile_no',
            'user__is_active',
            'course__name',
            'user__date_joined').distinct()
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)
    wb.save(response)
    return response

@check_admin_required
def CompetitiveCoursesUserDataExportCsv(request):
    filter_val = request.GET.get('filter','')
    response = HttpResponse(content_type='text/csv')
    file_name = f'UserData{str(datetime.datetime.now())}.csv'
    response['Content-Disposition'] = 'attachment; filename='+file_name
    writer = csv.writer(response)
    writer.writerow(['Email','Full Name','Gender','Mobile No.','Verification Status','Applied List','Created at'])

    rows = CompetitiveCourseApplied.objects.filter(user__is_superuser=False,course__name__contains=filter_val).annotate(
        first_name=F('user__first_name'),
        last_name=F('user__last_name'),
        full_name=Coalesce(Concat(Cast('first_name', CharField()), Value(' '), Cast('last_name', CharField())), 'first_name')
        ).values_list(
            'user__email',
            'full_name',
            'user__userprofile__gender',
            'user__userprofile__mobile_no',
            'user__is_active',
            'course__name',
            'user__date_joined').distinct()

    for row in rows:
        writer.writerow(row)

    return response