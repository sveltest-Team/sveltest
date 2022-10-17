#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""

                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|


"""
import os

"""
    测试框架的全局常量配置及配置信息
    version: 1.0.0
"""



import platform


# BASE_DIR = BASE_DIR = Path(__file__).resolve().parent.parent


# 框架组件注册表
APPS_LIST = [

]

# 浏览器驱动配置路径
BROWSER_DRIVER_PATH = r"D:\python3"

# 指定chrome安装路径
BINARY_LOCATION = '/opt/google/chrome/google-chrome'



# linux下的chromedriver 路径
CHROME_DRIVER_BINARY = '/usr/bin/chromedriver' # 指定chrome安装路径


if(platform.system() == 'Linux'):

    BINARY_LOCATION = '/usr/bin/chromedriver'  # 指定chrome浏览器驱动路径


# 错误重跑次数
TEST_CASE_ERROR_RETRY = 2


#错误截图
SCREENSHOTS_STATE = True


# 本地测试
DEBUG = True

# #测试用例场景路径
# TEST_CASE_FILE_PATH =  os.path.join(BASE,'data/case.xlsx').replace("\\",'/')
#
# # 定义日志文件的路径
# LOG_PATH = os.path.join(BASE,'report/logs').replace('\\','/')
#
# #测试结果
# TEST_CASE_RUN_REPORT = os.path.join(BASE,'report/html').replace('\\','/')
#
# # Test report compressed storage directory
# # 测试报告压缩的文件存放路径
# TEST_REPORT_COMPRESSED_STORAGE = None
#

# # Abnormal screenshot
# # 异常截图存放路径
SCREENSHOTS_SAVE_PATH = None

# 日志路徑
LOG_FILE_PATH = ''


# 日志状态
LOGGING_STATUS = False

# 日志输出的等级 1-3
LOGGING_VERBOSITY = 1

#测试结果
# TEST_CASE_RUN_REPORT = []

# 测试报告
TEST_REPORT = []


# # 识别图片集
# TEST_IMG_FILE_PATH = []


default_log_file = []


# # 测试用例集路径
CASE_SUITE_PATH = None

# 测试用例收集
COLLECT_STATUS = False

# ML_HTML_REPORT_STATUS = True


# 数据库配置
DATABASE = {
    "default":{
        # 会自动进行联想python 包
        "BACKEND":"redis",
        "LOCATION":"127.0.0.1:6379",
        "OPTIONS":{
            "PASSWORD":"",
            "DB":0
        },

    }
}


###########
#  EMAIL  #
###########

# Host for sending email.
# 发送邮件的主机号
EMAIL_HOST = 'localhost'

# Port for sending email.
# 发送邮件的服务端口
EMAIL_PORT = 25


# 可选的邮件配置
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None

EMAIL_TIMEOUT = None


# 自动邮箱状态
AUTO_SEND_EMAIL = True

# 邮件发送人
EMAIL_CONFIG = {
    "PORT":'smtp.163.com',
    "USERNAME":"gfl13453001@163.com",
    "LISTS":["guanfl@jideos.com","gfl13453001@163.com"],
    "CC_LIST":[],
    "PWD":"OTYWVZMZMBGWEYHJ",
    "TEMPLATE":"",
    "BACKEND":"",
    # 发送邮件成功后接收到的标题前缀
    "EMAIL_SUBJECT_PREFIX":'[sveltest] ',
    "TITLE":'自动化测试报告',
    "BCC_LISTS":[],
    "CONTENT":["测试报告"],
    "FILE":[],
}

# 测试执行环境
TEST_RUN_ENV = "sit"

# api模板服务
API_TEST_TEMPLATE = True

# web前端模拟
WEB_TEMPLATE = False


#############
#  LOGGING  #
#############

# The callable to use to configure logging
LOGGING_CONFIG = 'logging.config.dictConfig'

# Custom logging configuration.
LOGGING = {}



# 扩展程序列表
EXTENDERS_APP_LISTS = []

# 认证器默认配置
AUTHENTICATOR_CLASSES_CONFIG = {
    "CLASSES":  [
        # 默认的认证器
        "src.multiplex.core.components.auth.TokenAuth"
    ],
    "TOKEN":None
}



# 数据驱动数据源
DATA_DRIVER_SOURCE = {
    "DEFAULT_DATA_SOURCE":{
        "TYPE":"Excel",
        "PATH":None
    }
}


DEV = "dev"
DEV_HOST = ["127.0.0.1"]
DEV_PORT = [8000]

SIT = "sit"
SIT_ENV = []
SIT_PORT = [8080]

UAT = "uat"
UAT_ENV = []
UAT_PORT = [8000]

PROD = "prod"
PROD_ENV = []
PROD_PORT = [80]


# 环境控制器配置
ENVIRONMENT_CLASSES_CONFIG = {
    "CLASSES":[
        ""
    ],
    "DEFAULT_ENVIRONMENT_NAME":DEV,
    "ENVIRONMENT_HOST":DEV_HOST,
    "ENVIRONMENT_PORT":DEV_PORT,
}


# 测试用例运行匹配规则
TEST_CASE_ENFORCE_RULES = "test_*.py"

# 测试用例加载标记
TEST_METHOD_PREFIX = "test"

###########
# CI      #
###########
# 持续集成相关配置
CI_START = False

# 触发规则
CI_RULE = "cron"

# cron 表达式
CI_CRON_EXPRESSION = "*"


# 数据mock 默认语言
DATA_MOCK_LANGUAGE = "zh_CN"


######################
# 钉钉群机器人通知      #
######################
# 本地测试用的钉钉群机器人配置信息
DINGDING_WEBHOOK_DEV = {
    "URL": "https://oapi.dingtalk.com/robot/send?access_token={}",
    "SECRET": "SECf204470dbbd151188c50bb903ee1a57e6396a3a3e52288af8749d0744daa50e6",
    "KEYWORD": "自动化测试报告",
}
# 钉钉发送的模板类型
DINGDING_WEBHOOK_TEMPLATE = ""

# 用于生产上的钉钉群机器人配置
DINGDING_WEBHOOK_PROD = {}


# webdriver 测试配置
WEBDRIVER_TEST_SETTINGS = {
    "GLOBAL_IMPLICITLY_WAIT":3,
    "User-Agent":3,
    "headless":False,
    "proxy-server":None,
}


#  windows toast
WINDOWS_TOAST_STATUS = True
