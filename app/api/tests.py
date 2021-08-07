from django.test import TestCase

# Create your tests here.
import requests
import  time

def get_funcname(flag=''):
    def show_time(f):
        def inner(*x):
            start=time.time()
            f(*x)
            end =time.time()
            print("spend %s"%(end-start))
            if flag == 'true':
                pass
        return inner
    return show_time

class ApiTest:

    def __init__(self):
        self.baseurl = "http://127.0.0.1:8000/api/"

    @get_funcname('true')
    def test_index(self,path=None):
        r = requests.get(self.baseurl)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_add_one(self,path=None):
        print(self.baseurl+path)
        r = requests.get(self.baseurl+path)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_uid(self,path):
        uid = "1"
        print(self.baseurl+path+uid)
        r = requests.get(self.baseurl+path+uid)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_user(self,path):
        name = "tom"
        r = requests.get(self.baseurl+path+name)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_search(self,path):
        payload = {"q": "selenium"}
        # path = "search/"
        r = requests.get(self.baseurl+path, params=payload)
        result = r.json()
        print("result1",result)

    @get_funcname('true')
    def test_login_from(self,path):
        payload = {"username": "admin", "password": "a123456"}
        print(self.baseurl+path)
        r = requests.post(self.baseurl+path,data=payload)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_add_user_json(self,path):
        payload = {"name": "jack", "age": 22, "height": 177}
        r = requests.post(self.baseurl+path, json=payload)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_getheaders(self,path):
        headers = {"Content-Type": "application/json",
                   "token": "3d80caXELzU1aWmHwxl0TzW7jtterObm8l5EeAfipnhyaKmhFl8KdhFRvy4"}
        print(self.baseurl+path)
        r = requests.post(self.baseurl+path, headers=headers)
        # result = r.json()
        print(r.text)

    @get_funcname('true')
    def test_auth(self,path):
        auth = ("admin", "admin123")
        r = requests.post(self.baseurl+path, auth=auth)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_upload(self,path):
        files = {'file': open('./11.jpg', 'rb')}
        print(self.baseurl+path)
        r = requests.post(self.baseurl+path, files=files)
        print(r.text)



    @get_funcname('true')
    def test_upload(self,path):
        r = requests.get(self.baseurl+path, stream=True)
        print(r.text)
        with open("./log.jpg", "wb") as f:
            for chunk in r.iter_content(chunk_size=512):
                f.write(chunk)

    @get_funcname('true')
    def test_phone_get(self,path):
        print(self.baseurl+path)
        r = requests.get(self.baseurl+path)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_phone_put(self,path):
        print(self.baseurl+path)
        data={"name":"华为手机", "price": "3999"}
        r = requests.put(self.baseurl+path,data=data)
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_phone_delete(self,path):
        print(self.baseurl+path)
        r = requests.delete(self.baseurl+path )
        result = r.json()
        print(result)

    @get_funcname('true')
    def test_user_login_session(self,path):
        s = requests.Session()
        r = s.post(self.baseurl+path, data={"username": "jack", "password": "123"})
        result = r.json()
        print(result)

        r2 = s.get("http://127.0.0.1:8000/api/user_data/")
        result2 = r2.json()
        print(result2)

    @get_funcname('true')
    def test_activity_id_hasdata(self,path):
        data = {"aid": 1, "uid": 1}
        r = requests.post(self.baseurl+path, data=data)
        result = r.json()
        print(result)

    def test_activity_id_notdata(self,path):
        r = requests.post(self.baseurl+path)
        result = r.json()
        print(result)

if __name__ == "__main__":
    testload = ApiTest()
    # testload.test_index("aa")
    # testload.test_add_one("add_one/")
    # testload.test_uid("id/")
    # testload.test_user("user/")
    # testload.test_search("search/")
    # testload.test_login_from("login/")
    # testload.test_add_user_json("add_user/")
    # testload.test_getheaders("header/")
    # testload.test_getheaders("auth/")
    # testload.test_upload("upload_file/")
    # testload.test_upload("download/")
    # testload.test_phone_get("phone/1/")
    # testload.test_phone_put("phone/1/")
    # testload.test_user_login_session("user_login/")
    testload.test_activity_id_hasdata("activity_id/")
    testload.test_activity_id_notdata("activity_id/")