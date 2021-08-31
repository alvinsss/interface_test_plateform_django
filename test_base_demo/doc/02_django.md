## django 基本的模式

app.py

run app.py

## django 处理流程

1. 请求一个URL
http://127.0.0.1:8000/hello/

2. settings.py 默认的路由文件
```
ROOT_URLCONF = 'test_platform.urls'
```

3. `urls` 配置路由

```py
from django.urls import path
from demo_app import views


urlpatterns = [
    path('hello/', views.hello),
]
```

4. `view.py` 视图文件进行处理

```py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello, django")
```

## django MTV 模式

* mvc

m - model模型：数据库

v - viwe 视图：HTML页面

c - control 控制层：获取请求（HTML页面）做一些处理（操作到数据库），处理的结果返回


MTV

m - m  model
t - v  template 模板 （HTML页面）
v - c  view 


## web开发的三种模式

前端      后端
家        政府单位

* 第一种模式（没有接口）django：
家   --人->  办理
家   <--人-  办理
家   --人(身份证)->  办理
家   <--人-  办理
家   --人(身份证、户口本)->  办理
家   <--人-  办理
家   --人(身份证、户口本、单位证明)->  办理


第二种模式（电话=接口）django + js(jquery(ajax))：
家   --人->  办理
家(人)   <--电话-  （人）办理
家(人)   --身份证->  （人）办理
家(人)   <--电话-  （人）办理
家(人)   --户口本->  （人）办理
家(人)   <--电话-  （人）办理
家(人)   --单位证明->  （人）办理

第三种模式（所有的数据都是接口交互）django + vue.js(axios)：
家(人) --电话->  办理
家(人)  <--电话-  办理
家(人)  --身份证、户口本、单位证明->  （人）办理
家(人)  --电话->  （人）办理


### 第一种开发模式

`calculator.html`

```html
<h1>计算器</h1><br>

<form action="/calculator/" method="post">
    <input type="text" name="number_a" value=""> +
    <input type="text" name="number_b" value=""> =  {{ result }}
    <input type="submit" value="计算">
</form>
```

通过表单发送请求

* `action="/calculator/"` 指定请求的路径
* `method="post"` 指定请求的方法，get、post
* `name="number_a"` 和`name="number_b"` 参数的key


`vews.py`

```py
def calculator(request):
    """
    计算器
    """
    if request.method == "GET":
        return render(request, "demo_app/calculator.html")
    if request.method == "POST":
        a = request.POST.get("number_a")
        b = request.POST.get("number_b")
        count = int(a) + int(b)
        return render(request, "demo_app/calculator.html", {"result": count})
```

* GET 请求返回计算页面
* POST 请求返回请求页面和计算结果
* `request.POST.get("number_a")` 获取 POST请求的数据。



### 第二种开发模式

`calculator.html`

```html
<h1>计算器</h1><br>
<input type="text" id="number_a" value=""> +
<input type="text" id="number_b" value=""> = <span id="result"></span>
<button onclick="count()">计算</button>

<script src="http://code.jquery.com/jquery-2.1.1.min.js"></script>
<script>
    function count() {
        var numberA = $("#number_a").val()
        var numberB = $("#number_b").val()
        // window.alert("点击了计算按钮")
        $.post("/api/add/",{
            number_a: numberA,
            number_b: numberB
        },function(result){
            document.querySelector("#result").innerText = result.data.count;
        });
    }

</script>
```

* onclick 给按钮绑定一个方法。
* ` $.post()` 通过ajax 调用一个post请求。


`views.py`

```py
def calculator(request):
    """
    计算器
    """
    if request.method == "GET":
        return render(request, "demo_app/calculator.html")
```

后端需要返回页面。

`calculator_api.py`

```py
from django.http import JsonResponse


def add(request):
    """
    计算加法
    """
    if request.method == "POST":
        a = request.POST.get("number_a", "")
        b = request.POST.get("number_b", "")
        print("ab", a, b)
        if a == "" or b == "":
            return JsonResponse({"success": False, "message": "参数错误"})
        count = int(a) + int(b)
        return JsonResponse({"success": True, "message": "", "data": {"count": count}})
    else:
        return JsonResponse({"success": False, "message": "请求方法错误"})

```

实现一个加法运算的接口，前端通过ajax 调用时触发。

