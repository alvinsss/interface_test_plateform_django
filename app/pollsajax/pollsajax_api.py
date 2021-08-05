# -*- coding: utf-8 -*-
# @Time    : 2021/7/19 10:34
# @Author  : alvin
# @File    : pollsajax_api.py
# @Software: PyCharm
from django.http import JsonResponse
from app.polls.models import  Question
def  getplist (request):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
    '''获取投票内容'''
    if request.method == "POST":
        # print(Question.objects.order_by('-pub_date')[:3])
        queryset_info = Question.objects.order_by('-pub_date')[:3]
        queryset_list = list((queryset_info.values('id','question_text')))
        return JsonResponse({"success":True,"message":"111",
                             "data ":queryset_list })
    else:
        return JsonResponse({"success":False,"message":"请求错误！"})