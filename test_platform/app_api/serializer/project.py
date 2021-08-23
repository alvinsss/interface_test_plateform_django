# -*- coding: utf-8 -*-
# @Time    : 2021/8/23 17:44
# @Author  : alvin
# @File    : project.py
# @Software: PyCharm
from rest_framework import serializers

class ProjectValidator(serializers.Serializer):
    name = serializers.CharField(required=True,error_messages={"required":"name不能为空"})

