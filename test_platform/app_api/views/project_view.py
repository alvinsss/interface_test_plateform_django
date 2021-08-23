# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:25
# @Author  : alvin
# @File    : project_view.py
# @Software: PyCharm

from django.shortcuts import render
from rest_framework.views import  APIView
from django.http import JsonResponse
from app_api.serializer.project import ProjectValidator

def index(request):
    print("rest_app index!")
    return JsonResponse( {"msg":"it works!"})

class ProjectView(APIView):

    def get(self, request, *args, **kwargs):
        """
        查询 uid有值查单条 没值查询全部数据
        """
        return JsonResponse( {"msg":"pro test get"})
    def post(self, request, *args, **kwargs):
        """
        添加
        """
        name = request.data.get("name","")
        print(request.data)
        val = ProjectValidator(data=request.data)
        print(val)
        if val.is_valid():
            val.save()
        else:
            print(val.errors)
            return JsonResponse({"msg":"添加","error":val.errors})
        return JsonResponse( {"msg":"post works!"})

    def put(self, request, *args, **kwargs):
        """
        更新
        """
        return JsonResponse( {"msg":"it works!"})

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        return JsonResponse( {"msg":"it works!"})

