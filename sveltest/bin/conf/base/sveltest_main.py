#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 2021/10/28

"""


                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|



sveltest

"""



import argparse
import os
import sys

from sveltest.support import StFile
from sveltest.support import ReNumber
from sveltest.bin.conf.base import BASE_DIRs





st_os = StFile()

"""
v1.0.2
guanfl
20220926
"""

v = ''
if sys.platform == "win32" or sys.platform != "Linux":
    v = "sveltest@Windows 1.2  win32_x86\nUpdateTime:20221020\n version 1.2.0"
else:
    v = "sveltest@Linux 1.2  Linux32 \nUpdateTime:20221020\n version 1.2.0"

# try:
text_logo = """
                       _  _              _
                      | || |            | |
      ___ __   __ ___ | || |_  ___  ___ | |_
     / __|\ \ / // _ \| || __|/ _ \/ __|| __|
     \__ \ \ V /|  __/| || |_|  __/\__ \| |_
     |___/  \_/  \___||_| \__|\___||___/ \__|


                                            
            
sveltest 专注于让自动化更简洁、更简单、高效率！！！
输入 sveltest -h 命令你可以进行查看 sveltest cli的所有命令哦。

你也可以进行浏览器输入 sveltest 官方教程文档 ： https://sveltest-team.github.io/docs/
那么我们开始体验下吧！！！
"""

parser = argparse.ArgumentParser(
    usage="sveltest V1 cli",
    description='='*18+'sveltest-CLI'+'='*18,
                                 epilog='='*20+'sveltest'+'='*20)
parser.add_argument('create', help="创建工程 ", type=str,nargs='?')
# parser.add_argument('script', help="生成脚本 ",type=str,nargs='?') #可选的位置参数
parser.add_argument('run', help="运行脚本 ",type=str,nargs='?') #可选的位置参数
parser.add_argument('runserver', help="运行服务 ",type=str,nargs='?') #可选的位置参数
parser.add_argument('doc', help="浏览器打开sveltest 官方文档 ",type=str,nargs='?') #可选的位置参数
# ----------------------------------------------------------------

parser.add_argument('-ui', help='创建ui自动化工程项目模板 ',dest="ui")
# parser.add_argument('-api', help='创建api自动化工程项目模板 ',type=str)
# parser.add_argument('-T','--type', help='生成的脚本类型-暂指定仅为Python脚本 ')
# parser.add_argument('-file', help='源文件',type=str)
parser.add_argument('-p','--port', help='指定端口号')
# parser.add_argument('-template', help='创建一个关键字模板',required=False)
# parser.add_argument('-path', help='脚本存放目录路径')
parser.add_argument('-run', help='运行服务')
parser.add_argument('-v', "--version",action='version', version=v,help='查看版本')

# ------------------------------------------------------------------
args = parser.parse_args()


def main():

    try:

        if args.create == "create":
            current_path = os.path.abspath("")
            # 获取用户的当前路径
            # 获取当前文件的父级目录名称
            BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))

            if args.ui:
                path_join = os.path.join(current_path, args.ui).replace("\\","/")
                print("==>",path_join)

                t = ReNumber()
                if  t.number(args.ui) is False :
                    copy_fileName = os.path.join(BASE_DIRs, "project_template").replace("\\","/")

                    # print(BASE_DIR,sys.argv[-1])

                    if os.path.isdir(path_join):
                        print(args.ui,"该目录已存在")
                        # tank_os.copy_all(copy_fileName, path_join)
                        # for wi in os.walk(path_join):
                        #     print(os.path.isdir(path_join))
                        return copy_fileName
                    else:
                        os.mkdir(args.ui)
                        # 进行复制模板到用户的指定目录下
                        st_os.copy_all(copy_fileName, path_join)

                        for rootdir,sub,current_file in os.walk(path_join):

                            # 为了兼容linux系统需要对其进行格式转换
                            cr = rootdir.replace("\\","/").split("/")

                            # 进行遍历每一个目录下的文件
                            for file in current_file:
                                # 并进行拼接他们的文件路径

                                file_name_list = ["manage.py-tpl","__init__.py-tpl","BaiduElement.py-tpl"]

                                if file in file_name_list:

                                    _join_path = os.path.join(rootdir, file).replace("\\",'/')

                                    with open(_join_path,"r",encoding="utf-8") as f:
                                        text = f.read()
                                        #
                                    apps = text.format(filename=args.ui)
                                    with open(_join_path,'w',encoding="utf-8") as d:
                                        d.write(str(apps))
                                        d.close()
                                # #
                                _join_path = os.path.join(rootdir, file)
                                _sd = _join_path.split("-")
                                os.rename(_join_path,_sd[0])

                            if cr[-1] == "project_name":
                                _prod = rootdir.split("\\")[:-1]
                                join_path_string = "\\".join(_prod)
                                dir_path = os.path.join(str(join_path_string),sys.argv[-1])
                                os.rename(rootdir,dir_path)
                else:
                    print("ui参数值不能为数字")

            # if args.api:
            #     t = ReNumber()
            #     path_join = r"%s\%s" % (current_path, args.api)
            #     if t.number(args.api) is False:
            #         copy_fileName = os.path.join(BASE_DIR, r"config\api_project_template")
            #         # print(BASE_DIR,sys.argv[-1])
            #
            #         if os.path.isdir(path_join):
            #             print(args.api, "该目录已存在")
            #             # tank_os.copy_all(copy_fileName, path_join)
            #             # for wi in os.walk(path_join):
            #             #     print(os.path.isdir(path_join))
            #             return copy_fileName
            #         else:
            #             # print("ui",copy_fileName)
            #             os.mkdir(args.api)
            #             # 进行复制模板到用户的指定目录下
            #             st_os.copy_all(copy_fileName, path_join)
            #
            #             for rootdir, sub, current_file in os.walk(path_join):
            #
            #                 # 为了兼容linux系统需要对其进行格式转换
            #                 cr = rootdir.replace("\\", "/").split("/")
            #
            #                 # 进行遍历每一个目录下的文件
            #                 for file in current_file:
            #                     # 并进行拼接他们的文件路径
            #
            #                     file_name_list = ["manage.py-tpl", "__init__.py-tpl", "tk_test_api.py-tpl"]
            #
            #                     if file in file_name_list:
            #                         _join_path = os.path.join(rootdir, file)
            #                         # print(rootdir+"\\%s"%file)
            #                         with open(rootdir + "\\%s" % file, "r", encoding="utf-8") as f:
            #                             text = f.read()
            #                             #
            #                         apps = text.format(filename=args.api)
            #                         with open(rootdir + "\\%s" % file, 'w', encoding="utf-8") as d:
            #                             d.write(str(apps))
            #                             d.close()
            #                     # #
            #                     _join_path = os.path.join(rootdir, file)
            #                     _sd = _join_path.split("-")
            #                     os.rename(_join_path, _sd[0])
            #
            #                 if cr[-1] == "project_name":
            #                     _prod = rootdir.split("\\")[:-1]
            #                     join_path_string = "\\".join(_prod)
            #                     dir_path = os.path.join(str(join_path_string), args.api)
            #                     os.rename(rootdir, dir_path)
            #     else:
            #         print("ui参数值不能为数字")

        # 启动接口服务 仅本地地址
        elif args.create == "runserver":
            # guanfl
            # 20210610

            # d = str(BASE_DIRs).replace("\\","/").split("/")
            d = os.path.join(BASE_DIRs,'api_demo').replace("\\",'/')
            # dp = '\\'.join(d[1:]).replace("\\",'/')
            if args.port:
                os.system(f"{d} uvicorn api:app  --port {args.port} --reload")
            else:
                # sd = '\\'.join(d).replace("\\",'/')
                os.system(fr"python {d}\api.py")

        # v 1.2.1
        elif args.create == "doc":
            os.system("start https://sveltest-team.github.io/docs/")



        # elif args.create == "script":
        #     # TODO:已完成 待测试
        #     # guanfl
        #     # 20210609
        #     # 获取用户的当前路径
        #     current_path = os.path.abspath("")
        #     path_join = None
        #
        #     if args.template == "0":
        #         BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        #         temp = os.path.join(BASE_DIR,r"default\keyword_template.xlsx")
        #         shutil.copyfile(temp, os.path.join(current_path, 'keyword_template.xlsx'))
        #
        #     if args.template != "0" and args.template is not None:
        #         BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        #         temp = os.path.join(BASE_DIR, r"default\keyword_template.xlsx")
        #         st_os.copy_all(temp, os.path.join(args.template, 'keyword_template.xlsx'))
        #
        #
        #     lab = None
        #
        #     if args.file is not None:
        #
        #         try:
        #             if os.path.exists(args.file) is False:
        #                 path_join = r"%s\%s" % (current_path, args.file)
        #             else:
        #                 path_join = args.file
        #
        #
        #             script_path = TankOpenExecl(file=path_join)
        #             # 获取表单的列和行数
        #             get_col_row = [script_path.max_row, script_path.max_col]
        #
        #             for d in range(len(script_path.get_sheets())):
        #                 # 进行限制没有进行修改工作表名将进行不出来代码生成
        #                 if script_path.get_sheets()[d][0:-1] != "Sheet" and script_path.get_sheets()[d] != "示例":
        #                     # 存储所有数据
        #                     data_all = []
        #
        #                     script_path.set_active(d)
        #
        #                     for c in range(0, get_col_row[0]):
        #                         # 存储每一行的数据
        #                         cs = []
        #                         for r in range(get_col_row[1]):
        #                             cs.append(script_path.cell(c + 1, r + 1))
        #                         # 每一行数据进行存储到所有数据列表中
        #                         data_all.append(cs)
        #
        #                     func_list = []
        #
        #                     save_file_path = None
        #                     if args.path:
        #                         save_file_path = os.path.join(args.path,f'{script_path.filename[d]}.py')
        #                     else:
        #                         save_file_path = f'{script_path.filename[d]}.py'
        #
        #                     with open(save_file_path, "w+", encoding="utf-8") as f:
        #
        #                         for s in range(len(data_all)):
        #                             if s != 0:
        #                                 if data_all[s][0] == "url":
        #                                     f.write("from selenium import webdriver\n")
        #                                     f.write("from selenium.webdriver.common.by import By\n")
        #                                     f.write("import time\n\n\n")
        #
        #                                     f.write(f"class {script_path.filename[d]}:\n\n")
        #                                     f.write(f"    def __init__(self):\n")
        #                                     url = str(data_all[s][1])
        #                                     try:
        #                                         note = data_all[s][2]
        #                                         if note: f.write(f"        #{note}\n")
        #                                     except:
        #                                         pass
        #                                     f.write(f"        self.url = '{url}'\n")
        #                                 if data_all[s][0] == "open":
        #                                     driver = data_all[s][1]
        #                                     try:
        #                                         note = data_all[s][2]
        #                                         if note: f.write(f"        #{note}\n")
        #                                     except:
        #                                         pass
        #
        #                                     if driver == "chrome" or driver == "Chrome":
        #                                         driver = "Chrome"
        #                                         f.write(f"        self.driver = webdriver.{driver}()\n")
        #
        #                                     if driver == "ie" or driver == "IE":
        #                                         f.write(f"        self.driver = webdriver.Ie()\n")
        #                                     f.write(f"        self.driver.get(self.url)\n\n")
        #
        #                                 if data_all[s][0] == "func":
        #                                     func_list.append(data_all[s][1])
        #                                     f.write(f"    def test_{data_all[s][1]}(self):\n")
        #
        #                                 if data_all[s][0] == "sleep":
        #                                     try:
        #                                         note = data_all[s][2]
        #                                         if note: f.write(f"        #{note}\n")
        #                                     except:
        #                                         pass
        #                                     f.write(f"        time.sleep(4)\n")
        #
        #                                 if data_all[s][0] == "input":
        #
        #                                     try:
        #                                         note = data_all[s][3]
        #                                         if note: f.write(f"        #{note}\n")
        #                                     except:
        #                                         pass
        #                                         # upper() #转换成大写
        #                                     element_by = str(data_all[s][1]).split("=")
        #                                     f.write(
        #                                         f"        self.driver.find_element(by=By.{element_by[0].upper()},value='{element_by[1]}').send_keys('{data_all[s][2]}')\n")
        #
        #                                 if data_all[s][0] == "end":
        #
        #                                     try:
        #                                         note = data_all[s][3]
        #                                         if note: f.write(f"        #{note}\n")
        #                                     except:
        #                                         pass
        #                                     try:
        #                                         f.write(
        #                                             f"\n\n\nif __name__ == '__main__':\n    case = {script_path.filename[d]}()\n    case.test_{func_list[0]}()\n")
        #                                     except:
        #                                         print("不允许在没有声明方法前进行使用end关键字")
        #                                     break
        #         except:
        #             print("你必须进行指定一个Excel文件或者绝对路径")

        elif args.create == "run":
            # 运行测试脚本
            current_path = os.path.abspath("").replace('\\','/')
            os.system("python manage.py")



        else:
            print("没有这个命令：" + sys.argv[1])
    except:
        print(text_logo)




if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        pass



