# -*- coding: utf-8 -*-
# @Time    : 2021/8/24 13:40
# @Author  : alvin
# @File    : pagination.py
# @Software: PyCharm
from rest_framework.pagination import  PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = 5
    # 最大显示100条
    max_page_size = 100
    #可以通过传入？page=2&size=10 改变默认每页显示的个数
    page_size_query_param = "size"
    page_query_param = "page"