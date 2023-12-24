"""DJANGO_WEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app01.views import depart, user, admin, account,  chart, upload, city, catch

urlpatterns = [
    # path('admin/', admin.site.urls),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    
    #主页
    path('homepage/', chart.chart_list),
    path('', chart.chart_list),

    # 登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),



    # 管理员的管理
    path('admin/list/', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # 部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/<int:nid>/delete/', depart.depart_delete),
    path('depart/multi/', depart.depart_multi),

    # 用户管理
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    path('user/<int:nid>/edit/', user.user_edit),
    path('user/<int:nid>/delete/', user.user_delete),



    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),
    path('chart/highcharts/', chart.highcharts),

    

    # 监测站管理
    path('city/list/', city.city_list),
    path('city/add/', city.city_add),
    path('city/<int:nid>/edit/', city.city_edit),
    path('city/<int:nid>/delete/', city.city_delete),
    path('city/<int:nid>/map/', city.city_map),
    path('city/map/all', city.city_map_all),
    

    #采集信息
    path('catch/list/', catch.catch_list),
    path('catch/add/', catch.catch_add),
    path('catch/<int:nid>/edit/', catch.catch_edit),
    path('catch/<int:nid>/delete/', catch.catch_delete),
    path('catch/<int:nid>/capture/', catch.catch_capture),
    path('catch/capture/all/', catch.catch_capture_all),


    

    # 上传文件
    # path('upload/list/', upload.upload_list),
    # path('upload/form/', upload.upload_form),
    # path('upload/modal/form/', upload.upload_modal_form),
    
    #调试
    # path('tt/', chart.tt),

]
