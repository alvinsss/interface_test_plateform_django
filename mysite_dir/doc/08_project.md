# 项目相关接口

## 定义模型

project 表

* name Str
* describe  str
* status boole
* is_delete boole False
* update_time
* create_time

```python
from django.db import models


# Create your models here.
class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称", max_length=50, null=False)
    describe = models.TextField("描述", null=True, default="")
    status = models.BooleanField("状态", null=True, default=True)
    is_delete = models.BooleanField("状态", null=True, default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```


## 项目验证器

```py
class ProjectValidator(serializers.Serializer):
    """
    项目的验证器
    """
    name = serializers.CharField(required=True, max_length=50,
                                 error_messages={"required": "name不能为空",
                                                 "invalid": "类型不对",
                                                 "max_length": "长度不能大于50"})
    describe = serializers.CharField(required=False)
    status = serializers.BooleanField(required=False)
    # aatype = serializers.ChoiceField(choices=aatype)  # 枚举

```

* required：是否必填
* max_length： 最大长度
* error_messages：定义错误提示

创建与更新：

```py
... 
    def create(self, validated_data):
        """
        创建
        """
        project = Project.objects.create(**validated_data)
        return project

    def update(self, instance, validated_data):
        """
        更新
        """
        instance.name = validated_data.get("name")
        instance.describe = validated_data.get("describe")
        instance.status = validated_data.get("status")
        instance.save()
        return instance
```

* instance - 更新的对象 - 从数据库里查出来的
* validated_data - 更新的数据 - 从request 里面


## 分页



```py
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    # 每页显示多少个
    page_size = 5
    # 最大页数不超过 20
    max_page_size = 100
    # 可以通过传入?page=2&size=3,改变默认每页显示的个数
    page_size_query_param = "size"
    # 获取页码数的
    page_query_param = "page"
```

* 定义分类类

```py
class ProjectView(APIView):

    def get(self, request, *args, **kwargs):
        """
        查询
        """
        project = Project.objects.filter(is_delete=False).all()
        pg = Pagination()
        page_data = pg.paginate_queryset(queryset=project, request=request, view=self)
        ser = ProjectSerializer(instance=page_data, many=True)
        return JsonResponse({"msg": "查询", "data": ser.data})

```

* 使用分页类
