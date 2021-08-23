# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 10:04
# @Author  : alvin
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from django.urls import path, re_path
from  app_api.views.project_view import index
from  app_api.views.project_view import ProjectView
#真正的Django项目中，可能有多个应用程序，Django如何区分它们之间的URL名称,向您
# 的URLconf添加名称空间，app_name要设置应用程序命名空间，模板文件需要同步加上名称空间
app_name = 'app_api'
urlpatterns = [
    path('',index ),#http://127.0.0.1:8000/api/
    path('v1/project/',ProjectView.as_view()),
]