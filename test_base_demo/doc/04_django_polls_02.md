## django 模板语言（了解）

```html
{% if error_message %}
    <p><strong>{{ error_message }}</strong></p>
{% endif %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
{% endfor %}
```

* `{% if error_message %} {% endif %}`: if 判断
* `{% for choice in question.choice_set.all %} {% endfor %}`: for 循环
* `{{error_message}}`: 定义变量


## django FVB vs CVB

__FBV vs CBV__

* FBV（function base views） 就是在视图里使用函数处理请求。
* CBV（class base views） 就是在视图里使用类处理请求。

__FBV demo__

* view.py

```py
from django.http import HttpResponse
from rest_framework.decorators import api_view

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
#

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

```

* urls.py

```py
from xx import  view
path("test/", view.detail)
path("test2/", view.results)
```

__CBV demo__

* view.py

```py
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

```

* urls.py

```py
from xx import  view

path('', views.IndexView.as_view(), name='index'),
path('<int:pk>/', views.DetailView.as_view(), name='detail'),
path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
```

## 使用css 样式的使用方式

1. 定义style属性
```html
<li><a style="color: green">
```

2. 定义class属性

```html
<li><a class="my-li-a">

<style>
    .my-li-a {
        color: green;
    }
</style>
```

2. 定义css文件

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

参考： https://docs.djangoproject.com/en/3.2/howto/static-files/

2.1. `settting.py` 文件设置

```
STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
```

2.2. 的HTML文件中引用

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

