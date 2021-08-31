from django.shortcuts import render
from django.http import  JsonResponse
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import  APIView
from app_test.rest_app.serializer import UserSerializer
from app_test.rest_app.common import response,Error

def index(request):
    print("rest_app index!")
    return JsonResponse( {"msg":"it works!"})

class UserView(APIView):

    def get(self, request, *args, **kwargs):
        """
        查询 uid有值查单条 没值查询全部数据
        """
        uid = kwargs.get("uid", "")
        if uid is not None:
            try:
                user = User.objects.get(pk=uid)
            except User.DoesNotExist:
                return response(error=Error.USER_ID_NULL)

            ser = UserSerializer(instance=user, many=False)
            return response(data=ser.data)
        else:
            users = User.objects.all()
            ser = UserSerializer(instance=users, many=True)
            return response(data=ser.data)

        # users_list = []
        # for user in users:
        # user_dict = {
        #     "url": "http://127.0.0.1/users/{}/".format(user.id),
        #     "username": user.username,
        #     "email": user.email,
        #     "is_staff": user.is_staff
        # }
        # users_list.append(model_to_dict(user))

    def post(self, request, *args, **kwargs):
        """
        添加
        """
        print("data", request.data)  # post -farm-data/www-urlendcode /json 取值
        print("query_params", request.query_params)  # get params参数
        print(request.data['name'])
        print("kwargs", kwargs.get("uid"))  # url取参数 /aip/<int:uid>/
        return JsonResponse({"msg": "添加"})

    def put(self, request, *args, **kwargs):
        """
        更新
        """
        return JsonResponse({"msge": "更新"})

    def delete(self, request, *args, **kwargs):
        """
        删除
        """
        return JsonResponse({"msge": "删除"})



# fvb vs cvb
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_view(request, format=None):
    """
     """
    if request.method == 'GET':
        return JsonResponse({"msge": "查询"})

    elif request.method == 'POST':
        return JsonResponse({"msge": "添加"})

    elif request.method == 'PUT':
        return JsonResponse({"msge": "更新"})

    elif request.method == 'DELETE':
        return JsonResponse({"msge": "删除"})
