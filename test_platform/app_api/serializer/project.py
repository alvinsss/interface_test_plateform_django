# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:44
# @Author  : alvin
# @File    : project.py
# @Software: PyCharm
from rest_framework import serializers
from app_api.models.project_model import  Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields =['name','describe','status']

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

    def update(self,instance,validated_data):
        """
        instance -更新对象 从数据库查询出来的
        validated_data -- 更新的数据 从request里面来的
        """
        instance.name = validated_data.get("name")
        instance.describe = validated_data.get("describe")
        instance.status = validated_data.get("status")
        instance.save() #这个save也需要使用
        return  instance
