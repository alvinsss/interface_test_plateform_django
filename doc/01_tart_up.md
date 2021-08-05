## 环境准备

__后端__

* python 3.6/3.7/3.8/3.9

https://www.python.org/

* django
```
> pip install Django==3.2.5
```

* 编辑器/IDE

pycharm 
https://www.jetbrains.com/pycharm/download/#section=windows

 VS code
https://code.visualstudio.com/

* git

https://git-scm.com/

* github
https://github.com/

1. 注册一个账号
2. 创建一个开源项目
3. 克隆到本地

git clone https://github.com/defnngj/test_dev05

* 练习
1. 参考官方例子，做投票项目
https://docs.djangoproject.com/en/3.2/

2. 提交到github，把地址发出来。


main  dev   test
      开发   测试

main: <--dev <--冲突--test  ok
main: <--test <--冲突--dev

main <<=== dev: <-冲突- test 
main <<=== test: <-冲突- dev

test <--- main
dev <--- main

dev <- 冲突-- main

