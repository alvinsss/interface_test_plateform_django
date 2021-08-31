# 接口测试平台

__项目管理__

* 获取列表接口（分页） 
* 添加项目接口
* 更新项目接口
* 删除项目接口

__模块管理__

* 获取模块列表接口（分页） 
* 添加模块接口
* 更新模块接口
* 删除模块接口

1. 项目 --> 模块 （一对多）


__用例管理__

* 获取用例列表接口（分页） 
* 调试接口 *
* 断言接口
* 添加用例接口
* 更新用例接口
* 删除用例接口
* 获取项目/模块的列表的接口 **

1. 项目 --> 模块--> 用例（一对多）


__任务管理__

* 获取任务列表接口（分页） 
* 获取项目/模块/用例 树形结构的接口 ** 
* 添加任务接口
* 更新任务接口
* 删除任务接口 
* 执行任务的接口 ***** celery队列/线程
* 测试报告接口 *** echarts

1. 任务 --> 报告 (一对多)


接口(id) --> excel 列：id

接口(name, password..) --> excel 列：name password ..

接口(email, ddd.) -->  excel email ddd ...


# todo list

* 后端项目 backend
  * 1.定义项目表结构
  * 2.实现项目相关接口
  * 3.接口的认证 

interface_management /backend
1. app_common: 放公共的功能：认证、用户登录、
2. app_api: 放接口


* 前端项目 frontend


## 接口定义规则

查询: get
添加：post
更新：put  
删除：delete

数据格式：统一用JSON , 除非文件上传下载。

/project/<int:pid>/  从两个地方取参数

{
    "name":"new name",
}

/porject/   这种会多一些

{
    "id": 1
    "name":"new name",
}


作业：
1. 现在 ProjectView 继承 APIView, 增加 MyAPIView(封装response)，
2. ProjectView 继承 MyAPIView
