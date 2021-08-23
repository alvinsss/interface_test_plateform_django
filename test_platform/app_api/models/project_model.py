from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField("名称",max_length=50,null=False)
    describe=models.TextField("描述",null=True,default="")
    status=models.BooleanField("状态",null=False,default=True)
    is_delete =models.BooleanField("状态",null=True,default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name