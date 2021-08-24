# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:25
# @Author  : alvin
# @File    : project_view.py
# @Software: PyCharm

from django.shortcuts import render
from rest_framework.views import  APIView
from django.http import JsonResponse
from app_api.serializer.project import ProjectValidator,ProjectSerializer
from app_api.models.project_model import Project

def index(request):
    print("rest_app index!")
    return JsonResponse( {"msg":"it works!"})

class ProjectView(APIView):

    def get(self, request, *args, **kwargs):
        """
        查询 uid有值查单条 没值查询全部数据
        """
        pid = kwargs.get("pid")
        if pid is not None:#从url获取到pid的话 查询指定pid数据
            try:
                project=Project.objects.get(pk=pid)
                ser = ProjectSerializer(instance=project,many=False)
            except Project.DoesNotExist:
                return JsonResponse( {"pid":"Project pid is Null"})
            return JsonResponse( {"msg":"get project is ok!","data":ser.data})
        else:
            project = Project.objects.all()
            ser = ProjectSerializer(instance=project,many=True)
            return JsonResponse( {"msg":"get project list is ok!","data":ser.data})

    def post(self, request, *args, **kwargs):
        """
        添加
        """
        name = request.data.get("name","")
        status = request.data.get("status","")
        describe = request.data.get("describe","")
        print(request.data)
        val = ProjectValidator(data=request.data)
        print(val)
        if val.is_valid():#判断验证的字段是否都对，参考serizlizer.project定义
            val.save() #保存数据
        else:
            print(val.errors)
            return JsonResponse({"msg":"添加","error":val.errors})
        return JsonResponse( {"msg":"增加项目名:{}成功".format(name)})

    def put(self, request, *args, **kwargs):
        """
        更新
        """
        # http://127.0.0.1:8000/api/v1/project/1/ 从url取数据，需要urls定义pid
        pid = kwargs.get("pid")
        if pid is None:
            return JsonResponse( {"pid":"pid is Null"})
        try:
            project=Project.objects.get(pk=pid)
        except Project.DoesNotExist:
            return JsonResponse( {"pid":"Project pid is Null"})
        val = ProjectValidator(instance=project,data=request.data)
        if val.is_valid():#判断验证的字段是否都对
            val.save() #保存数据  serializer update也需要save
        else:
            print(val.errors)
        return JsonResponse( {"msg":"update project is ok!"})

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        return JsonResponse( {"msg":"it works!"})

