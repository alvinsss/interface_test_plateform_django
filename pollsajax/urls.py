# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 10:04
# @Author  : alvin
# @File    : urls.py
# @Software: PyCharm
from django.urls import  path
from . import views
#真正的Django项目中，可能有多个应用程序，Django如何区分它们之间的URL名称,向您
# 的URLconf添加名称空间，app_name要设置应用程序命名空间，模板文件需要同步加上名称空间
app_name = 'pollsajax'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]