from django.db import models

# Create your models here.
from django.utils import timezone
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes =models.IntegerField(default=0)
    #__str__()方法，这不仅是为了您在处理交互式提示时的方便，还因为在Django的自动生成管理过程中使用了对象的表示。
    def __str__(self):
        return self.choice_text
