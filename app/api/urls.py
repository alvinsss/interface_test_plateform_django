# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 10:04
# @Author  : alvin
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from django.urls import path, re_path
from . import views
#真正的Django项目中，可能有多个应用程序，Django如何区分它们之间的URL名称,向您
# 的URLconf添加名称空间，app_name要设置应用程序命名空间，模板文件需要同步加上名称空间
app_name = 'api'
urlpatterns = [
    path('', views.index ),
    path( 'add_one/',views.add_one ),
    path('user/<str:username>/', views.getname),
    path('id/<int:uid>/', views.getuid),
    # http://127.0.0.1:8000/api/search1/q=sel
    re_path('^search1/q=(?P<q>\w+)',views.search1),
    path('search/',views.search),
    # http://127.0.0.1:8000/api/login1/username=admin&password=a123456
    re_path('^login1/username=(?P<username>\w+)&password=(?P<password>\w+)',views.login1),
    path('login/',views.login),
    # re_path('^add_user/name=(?P<name>\w+)&age=(?P<age>\w+)&height=(?P<height>\w+)',views.add_user),
    path('add_user/',views.add_user),
    #  http://127.0.0.1:8000/page=12&key=abc
    #  re_path('page=(?P<page>\d+)&key=(?P<key>\w+)', views.detail, name="detail"),
    # https://github.com/defnngj/learning-API-test/tree/master/flask_api
    path('header/',views.header),
    path('auth/',views.auth),
    path('upload/',views.upload),
    path('upload_file/',views.upload_file),
    url(r'^download/',views.download,name="download"),
]