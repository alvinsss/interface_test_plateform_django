# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:44
# @Author  : alvin
# @File    : project.py
# @Software: PyCharm
from rest_framework import serializers
from app_api.models.project_model import  Project

aatype=[1,2,3]
class ProjectValidator(serializers.Serializer):
    name = serializers.CharField(required=True,
                                 error_messages={"required":"name不能为空",
                                 "invalid":"类型不对",
                                 "max_length":"长度不能大于50"})
    describe = serializers.CharField(required=True,error_messages={"required":"describe不能为空"})
    status = serializers.BooleanField(required=True,error_messages={"required":"status不能为空"})
    # aatype = serializers.ChoiceField(choices=aatype)#枚举
    def create(self, validated_data):
        '''创建'''
        project = Project.objects.create(**validated_data)
        return project