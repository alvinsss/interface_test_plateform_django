import base64
import json
import  os
from django.http import JsonResponse, HttpResponse, FileResponse
# Create your views here.
from django.conf import settings
from werkzeug.utils import secure_filename


def index(request):
    return JsonResponse({"code":10200,"message":"i am work!"})

class Number:
    n = 0

#每次请求数字加1
def add_one(requset):
    print(requset)
    Number.n = Number.n +1
    return JsonResponse({"code":10200,"data":{ "number": Number.n },"message":"i am work!"})

#http://127.0.0.1:8000/api/user/tom/
def getname(request,username):
    if request.method == "GET":
        message = "hello {}".format(username)
        return JsonResponse({"code":10200,"message":message})
    else:
        return JsonResponse({"code":10200, "message":"method is not "})
#http://127.0.0.1:8000/api/uid/1/
def getuid(request,uid):
    if request.method == "GET":
        if 1 == uid:
            return JsonResponse({"code": 10200, "data": {"age": 22, "id": uid, "name": "tom"}, "message": "success"})
        else:
            return JsonResponse({"code": 10101, "message": "user id null"})
    else:
        return JsonResponse({"code":10200, "message":"method is not "})

def search1(request,q):
    print(q)
    if request.method == "GET":
        if len(q) > 0:
            return JsonResponse({"code": 10200, "data": ["selenium教程", "seleniumhq.org", "selenium环境安装"], "message": "success"})
        else:
            return JsonResponse({"code":10200, "message":" par is null"})
    else:
        return JsonResponse({"code":10200, "message":"method is not "})

def search(request):
    if request.method == "GET":
        search = request.GET.get("q")
        print(search)
        if len(search) > 0:
            return JsonResponse({"code": 10200, "data": ["selenium教程", "seleniumhq.org", "selenium环境安装"], "message": "success"})
        else:
            return JsonResponse({"code":10200, "message":" par is null"})
    else:
        return JsonResponse({"code":10200, "message":"method is not "})

def login1(request,username,password):
    print(username,password)
    if request.method == "POST":
        if username is None or password is None:
            return JsonResponse({"code": 10102, "message": "username or passwrord is None"})
        elif username == "" or password == "":
            return JsonResponse({"code": 10103, "message": "username or passwrord is null"})
        elif username == "admin" and password == "a123456":
            return JsonResponse({"code": 10200, "message": "login success"})
        else:
            return JsonResponse({"code": 10104, "message": "username or password error"})
    else:
        return JsonResponse({"code":10200, "message":"method is not "})


def login(request ):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        print(username,password)
        if username is None or password is None:
            return JsonResponse({"code": 10102, "message": "username or passwrord is None"})
        elif username == "" or password == "":
            return JsonResponse({"code": 10103, "message": "username or passwrord is null"})
        elif username == "admin" and password == "a123456":
            return JsonResponse({"code": 10200, "message": "login success"})
        else:
            return JsonResponse({"code": 10104, "message": "username or password error"})
    else:
        return JsonResponse({"code":10200, "message":"method is not "})


def add_user(request):
    # 原来是contentType为application/json时，Django不支持request.POST.get()，但可
    # 以通过request.body来获取string类型的参数
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "")
            age = data.get("age", "")
            height = data.get("height", "")
            print("add_user",name,age,height)
        except json.decoder.JSONDecodeError:
            return JsonResponse(10105, "format error")
        if name is None or age is None or height is None  :
            return JsonResponse(10102, "username or passwrord is None")
        elif name == "" or age == "" or height == "":
            return JsonResponse({"code": 10102, "message": "key null"})
        elif name == "":
            return JsonResponse({"code": 10103, "message": "name null"})
        elif name == "alvin":
            return JsonResponse({"code": 10104, "message": "name exist"})
        elif (len(name) and len(str(age)) and len(str(height)))>0:
            return JsonResponse({"code": 10200, "message": "add success",
                                 "data": {"age": age, "height": height, "name": name},})
        else:
            return JsonResponse(10104, "username or password error")
    else:
        return JsonResponse({"code":10200, "message":"method is not "})

def header(request):
    contentType = request.headers['Content-Type']
    token = request.headers['token']
    print(contentType,token,request.headers["User-Agent"])
    headers={
        "Content-Type": contentType,
        "token": token
    }
    return JsonResponse({"code":10200, "message":"header ok!","data":headers})

def auth(request):
    if request.method == 'POST':
        auth = request.headers.get("Authorization", '')
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        # print(request.META)
        print(auth,auth_header)
        return JsonResponse({"code": 10101, "message": "Authorization null"})
        # if auth is None:
        #     return JsonResponse(10101, "Authorization None")
        # else:
        #     auth = auth.split()
        #     auth_parts = base64.b64decode(auth[1]).decode('utf-8').partition(':')
        #     userid, password = auth_parts[0], auth_parts[2]
        #     if userid == "" or password == "":
        #         return JsonResponse(10102, "Authorization null")
        #     if userid == "admin" and password == "admin123":
        #         return JsonResponse(10200, "Authorization success!")
        #     else:
        #         return JsonResponse(10103, "Authorization fail!")
    else:
        return JsonResponse({10101, "request get  method error"})

def upload(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        print(request.FILES.get('files'))
        myFile =request.FILES.get("files", None)    # 获取上传的文件，如果没有文件，则默认为None
        print(myFile.name)
        if not myFile:
            return JsonResponse({"code": 10200, "message": "upload success!"})
        destination = open(os.path.join(settings.API_UPLOADFILE,myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return JsonResponse({"code": 10200, "message": "upload voer!"})


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in settings.ALLOWED_EXTENSIONS


def upload_file(request):
    if request.method == 'POST':
        f = request.FILES.get("files", None)
        print(f)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(settings.API_UPLOADFILE, filename))
            return  JsonResponse({"code": 10200, "message": "upload success!"})
        else:
            return  JsonResponse({"code": 10102,  "message": "file type error!"})

    else:
        return JsonResponse({"code": 10101,  "message": "request method error!"})

def download(request):
    if request.method == "GET":
        filename = "11.jpg"
        print((os.path.join(settings.API_UPLOADFILE, filename)))
        file = open((os.path.join(settings.API_UPLOADFILE, filename)),'rb')
        response = FileResponse(file)
        response['Content-Type']='application/octet-stream'
        response['Content-Disposition']="attachment;filename={}".format(filename)
        print(response)
        return response
    else:
        return JsonResponse({"code": 10101,  "message": "request method error!"})
