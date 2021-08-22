# django 投票系统精讲


## django Models定义

__定义一个模型__

```py
class Person(models.Model):
    LastName = models.CharField(max_length=30, default="admin", null=False)
    FirstName = models.CharField()
    Address = models.CharField(default="北京")
    Age = models.IntegerField(default=0)
    Status = models.BooleanField(default=True)
    CreateTime = models.DateTimeField(auto_now_add=True)
    UpdateTime = models.DateTimeField(auto_now=True)
```

* 常用字段类型：

`CharField`、`IntegerField`、`DateTimeField`、`BooleanField`、`TextField`、


* `max_length`： 定义字段长度
* `default`：定义字段默认值
* `null`：定义字段默认值，默认`Ture`可以为空，`False`不能为空。


__外键的关联__

```py
question = models.ForeignKey(Question, on_delete=models.CASCADE)
```

on_delete 几种模式：

* `on_delete=None`： 删除关联表中的数据时,当前表与其关联的field的行为

* `on_delete=models.CASCADE`： 删除关联数据,与之关联也删除

* `on_delete=models.DO_NOTHING`： 删除关联数据,什么也不做

* `on_delete=models.PROTECT`： 删除关联数据,引发错误ProtectedError

## django 模型同步

```shell
> python manage.py makemigrations polls
> python manage.py sqlmigrate polls 0001
> python manage.py migrate
```

* `makemigrations` 会在当前目录下生成一个migrations文件夹, 里面生成 `0001_xxx` 文件。
* `sqlmigrate xxx 0001` : 查看 `0001_xx`文件生成的SQL语句。
* `migrate`: 执行之前生成的migrations文件

1. 生成migrations文件不能随便删除。
2. 添加、修改新的字段需要重新执行上面的命令。
3. 如果添加的字段是必填，需要设置默认值。


## django 模型操作

* 查询所有的数据

```py
Question.objects.all()
```

* 根据条件查询

```py
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)
Question.objects.get(pk=2)
```

get() 查询
1. 如果匹配不到任何数据会抛异常
2. 如果匹配到多条数据也会抛异常
3. 只能查询出数据并且只有一条的情况下才是对的。

* 关联查询：通过问题查询关联的所有选项

```py
q = Question.objects.get(pk=1)
q.choice_set.all()
```

* 条件查询

```py
Choice.objects.filter(question__pub_date__year=current_year)
q.choice_set.filter(choice_text__startswith='Just hacking')
```

filter()
1. 查询结果为空，返回空对象。
2. 查询结果为多条，返回多个对象。


* 删除

```py
q = Question.objects.get(pk=1)
q.choice_set.filter(choice_text__startswith='Just hacking')
q.delete()
```


* 更新  

```py
# 方法一
q = Question.objects.get(pk=1)
q.question_text = "新的消息?"
q.save()

# 方法二
q = Question.objects.filter(question_text="what's new").update(question_text="新的消息?")

Project.objects.filter(name__contains='项目')

q.choice_set.all
```

* 创建

```py
#方法一
q = Question.objects.create(question_text="What's new?", pub_date=timezone.now())

# 创建选项1
q = Question.objects.get(pk=1)
Choice.objects.create(choice_text='Not much', question=q)

# 创建选项2
Choice.objects.create(choice_text='Not much', question_id=1)


# 方法二
q = Question(question_text="What's new?", pub_date=timezone.now())
q.choice_set.create(choice_text='Not much', votes=0)

```

## admin 使用

django提供了默认的admin后台

1. 创建进入后台的帐号：
```
 python .\manage.py createsuperuser
```

2. 进入后台：

http://127.0.0.1:8000/admin

3. 注册模型到后台
```py
# admin.py
from django.contrib import admin
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

```

## SqliteStudio下载：

* https://sqlitestudio.pl/


## 作业：
使用bootstrap美化投票系统：
https://v3.bootcss.com/examples/starter-template/


## 使用css 样式的集中方案

* 定义style属性
```html
<li><a style="color: green">
```

* 定义class属性

```html
<li><a class="my-li-a">

<style>
    .my-li-a {
        color: green;
    }
</style>
```

* 定义css文件

`style.css`

```css
li a {
    color: green;
}
```

`html`
```html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">

```

## 静态文件的使用

1. 使用在线的CDN

```html
<link href="https://coderthemes.com/hyper/creative/assets/css/icons.min.css" rel="stylesheet" type="text/css" />
<link href="https://coderthemes.com/hyper/creative/assets/css/app-creative.min.css" rel="stylesheet" type="text/css" id="light-style" />
<link href="https://coderthemes.com/hyper/creative/assets/css/app-creative-dark.min.css" rel="stylesheet" type="text/css" id="dark-style" />

<script src="http://code.jquery.com/jquery-migrate-1.2.1.min.js"></script>

```

2. 本地的样式库

> 先配置静态文件的路径

```html
{% load static %}
<link href="{% static 'css/icons.min.css' %}" rel="stylesheet" type="text/css" />
<link href="{% static 'css/app-creative.min.css' %}" rel="stylesheet" type="text/css" id="light-style" />
<link href="{% static 'css/app-creative-dark.min.css' %}" rel="stylesheet" type="text/css" id="dark-style" />
```

## 作业

练习：测试驱动开发的
https://github.com/defnngj/learning-API-test/tree/master/flask_api
https://github.com/defnngj/learning-API-test/blob/master/flask_api/api_server.py

