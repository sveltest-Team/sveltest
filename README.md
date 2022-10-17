[GitHub]() | [Gitee]() 

# sveltest 



> sveltest 是一个底层核心基于unittest扩展的，集成式框架、包含自动化测试模块、应用服务器、应用开发工具等
> 该`sveltest `框架使编写测试脚本变得容易、快捷，支持创建复杂的测试。

## Features

1、更为详细的测试执行结果输出、逼格逐渐提升。

2、与unittest无间隙对接、提供更为复杂的TestCase类。

3、完善的辅助功能助你快速搭建工程化项目、简单易于上手、过滤冗余功能体系。

4、更为丰富的参数化管理(数据随机化、可定制化、数据库参数化等)。

5、自动化下载驱动，无需自行去下载驱动程序一切操作均由fastTest来操作。




一个简单测试的demo：

```python
from sveltest import TestCase,main


class TestDemoTo1(TestCase):
    """简单的测试demo"""

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_case_demo(self):

        self.assertEqual("sveltest","sveltest")


if __name__ == '__main__':
    main(verbosity=1)
```

执行后的结果

```python

================================ 用例开始执行 =================================
test_case_demo (__main__.TestDemoTo1)   PASS
******************************** 测试结果汇总 *********************************
     执行结果     
┌────────┬───────┐
│ status │ count │
├────────┼───────┤
│ PASS   │ 1     │
│ FAIL   │ 0     │
│ SKIP   │ 0     │
│ ERROR  │ 0     │
│ COUNT  │ 1     │
└────────┴───────┘
================= 总共运行了 1 条测试用例  总共运行了 0.000s ==================
```

终端的结果:

 	![image](README.assets/143005934-83e7e617-a07a-4b77-8bef-97260931d1c7-16376623560173.png)



参数化实例：

```python



from sveltest import TestCase,main
from sveltest.core.components.parameterized import char,parameterized


@parameterized()
class TestDemoTo1(TestCase):
    """简单的测试demo"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @char("sweet","testcase")
    def test_case_demo(self,a):
        self.assertEqual("sweet",a,msg=666)


if __name__ == '__main__':
    main(verbosity=1)
    
```

内置参数化、提供多种可能性选择如：随机数据、自定义参数、数据库读取、文件数据读取等

```
================================ 用例开始执行 =================================
test_case_demo_1 (__main__.TestDemoTo1)   PASS
test_case_demo_2 (__main__.TestDemoTo1)   FAIL
-------------------------------- 铺抓到的异常 ---------------------------------
>>> test_case_demo_2 (__main__.TestDemoTo1)
Traceback (most recent call last):
  File "D:\python39\lib\site-packages\sweet\core\components\parameterized.py", 
line 446, in wrapper
    return func(self,*args, **kwargs)
  File "F:\app\test_case_666.py", line 90, in test_case_demo
    self.assertEqual("sweet",a,msg=666)
AssertionError: 'sweet' != 'testcase'
- sweet
+ testcase
 : 666

******************************** 测试结果汇总 *********************************
     执行结果     
┌────────┬───────┐
│ status │ count │
├────────┼───────┤
│ PASS   │ 1     │
│ FAIL   │ 1     │
│ SKIP   │ 0     │
│ ERROR  │ 0     │
│ COUNT  │ 2     │
└────────┴───────┘
================= 总共运行了 2 条测试用例  总共运行了 0.001s ==================

```



## 文档

有关完整文档，包括安装、教程和 PDF 文档，请参阅  https://sveltest-team.github.io/docs/






### 如果你在使用 sveltest 库发现bug请联系我 gfl13453001@163.com










​			
