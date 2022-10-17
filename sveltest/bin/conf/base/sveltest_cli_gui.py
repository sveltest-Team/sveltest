#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/11/8

"""
                   _  _              _
                  | || |            | |
  ___ __   __ ___ | || |_  ___  ___ | |_
 / __|\ \ / // _ \| || __|/ _ \/ __|| __|
 \__ \ \ V /|  __/| || |_|  __/\__ \| |_
 |___/  \_/  \___||_| \__|\___||___/ \__|
"""
import argparse
import os
import subprocess

from gooey import Gooey, GooeyParser, PrefixTokenizers


@Gooey(
    program_name="fastTest-CLI GUI TOOL",
    language="chinese",
    image_dir=r"F:\app\1",
    # tabbed_groups=True,
    advanced=True,
    sidebar_title="命令",
    show_sidebar=True, navigation=["Tabbed"],
    menu=[
        {'name': '关于', 'items': [{
            'type': 'AboutDialog',
            'menuTitle': '关于',
            'name': 'fastTest-CLI GUI TOOLS',
            'description': '                  fastTest 框架\n给你带来快速搭建测试项目的极速体验',
            'version': '1.0.0',
            'copyright': '2021',
            'website': 'https://github.com/chriskiehl/Gooey',
            'developer': '',
            'license': 'MIT'
        },
        ]}, {
            'name': '帮助',
            'items': [{
                'type': 'Link',
                'menuTitle': '教程文档',
                'url': 'https://www.readthedocs.com/foo'
            }]
        }],

)
# @Gooey(menu=[
# 	{'name': '文件', 'items': [{
#                 'type': 'AboutDialog',
#                 'menuTitle': 'About',
#                 'name': 'Gooey Layout Demo',
#                 'description': 'An example of Gooey\'s layout flexibility',
#                 'version': '1.2.1',
#                 'copyright': '2018',
#                 'website': 'https://github.com/chriskiehl/Gooey',
#                 'developer': 'http://chriskiehl.com/',
#                 'license': 'MIT'
#             },
# 	]},
#              {'name': 'Tools', 'items': []},
#              {'name': 'Help', 'items': []}],
# 	   language="chinese"
# 	   )

def main():
    parser = GooeyParser(description="fastTest CLI GUI")

    # 子命令
    # parser.add_argument("--create",help='创建工程', dest='create',)
    subs = parser.add_subparsers(help='创建工程', dest='create')
    # add_subparsers(help='commands', dest='command')
    create_parser = subs.add_parser(
        'create', help='创建WEB UI自动化测试工程项目')

    create_parser.add_argument('-type',
                               widget='Dropdown',
                               help='创建的项目类型(ui/api/qt)',
                               type=str,
                               metavar='type',
                               choices=["ui", "api", "app", "qt"],
                               default="ui"
                               )
    create_parser.add_argument('file_path', widget='DirChooser',
                               help='选择需要的目录', type=str,
							   gooey_options={
								   # 输入验证
								   'validator': {
									   # 表单验证规则
									   'test': 'len(user_input) > 0',
									   # 验证描述信息
									   'message': '该选项不能为空'
								   }
							   })

    # 	curl_parser.add_argument('filepath', widget='DirChooser',
    # 						help='选择需要的目录',type=argparse.FileType())
    create_parser.add_argument('project_name', widget='TextField',
                               help='工程项目名称')
    # parser.add_argument('filepath', widget="DirChooser")      # 文件选择框
    # parser.add_argument('val', widget="TextField")      # 文件选择框
    # parser.add_argument('Date', widget="DateChooser")          # 日期选择框

    # ==================================================================
    # add_subparsers(help='commands', dest='command')
    docs_parser = subs.add_parser(
        'open_docs', help='浏览器打开 fastTest 官方教程文档及官方网站')
    docs_parser.add_argument('-doc', action="store_true",
    						 help='直接点击开始即可',default=True)
    # curl_parser.add_argument('val', widget='TextField',
    # 						 help='Option one')

    #===================================================================



    webservice_parser = subs.add_parser(
        'webservice', help='web 服务')
    group3 = webservice_parser.add_argument_group('创建服务类型')
    group3.add_argument('type',
                               widget='Dropdown',
                               help='创建服务类型(接口服务则需要填写分组为接口服务的参数、本地服务器则填写文件服务器分组的配置信息)',
                               type=str,
                               metavar='类型',
                               choices=["接口服务", "本地服务器"],
                               default="接口服务"
                               )

    group1 = webservice_parser.add_argument_group('接口服务')
    # group1.add_argument('--opt1', action='store_true',
    #                     help='Option one')


    # stuff = group1.add_mutually_exclusive_group(
    #     required=True,
    #     gooey_options={
    #         'initial_selection': 0
    #     }
    # )
    group1.add_argument('host', widget="TextField",
    						 help='主机ip',default="0.0.0.0",type=str)

    group1.add_argument('-port', widget="TextField",
    						 help='端口',default="8100",type=str)

    group2 = webservice_parser.add_argument_group('文件服务器')
    group2.add_argument('-H', widget="TextField",
                        help='主机ip', default="0.0.0.0", type=str)
    group2.add_argument('-p', widget="TextField",
    						 help='端口',default="8160",type=str)
    group2.add_argument('-root_dir', widget='DirChooser',

                               help='选择一个目录作为服务器的根目录', type=str,
                               gooey_options={
                                   # 输入验证
                                   'validator': {
                                       # 表单验证规则
                                       'test': 'len(user_input) > 0',
                                       # 验证描述信息
                                       'message': '该选项不能为空'
                                   }
                               })

    # ===================================================================
    # download
    download_parser = subs.add_parser(
        'download', help='下载工具'
    )
    group2 = download_parser.add_argument_group('第三方依赖包下载')
    # group2.add_argument('type',
    #                            widget='Listbox',
    #                            help='选择需要下载的Python(第三方包)依赖',
    #                            type=str,
    #                            metavar='类型',
    #                            choices=["接口服务", "本地服务器"],
    #                            default="接口服务",
    #                              nargs="*"
    #                            )

    group2.add_argument(
        "-P",
        "--package",
        metavar='第三方库',
        help='选择需要下载的Python(第三方包)依赖',
        choices=["Django","Selenium2","Selenium3","redis","tomorrow"],
        widget='FilterableDropdown',
        gooey_options={
            'label_color': (255, 100, 100),
            'placeholder': '可以进行输入关键字进行搜索对应的包',
            'search_strategy': {
                'type': 'PrefixFilter',
                'choice_tokenizer': PrefixTokenizers.WORDS,
                'input_tokenizer': PrefixTokenizers.REGEX('\s'),
                'ignore_case': True,
                'operator': 'AND',
                'index_suffix': False  # set to True to enable substring searching!
            }
        })

    group = download_parser.add_argument_group('选择下载源')
    group.add_argument('type',
                               widget='Dropdown',
                               help='选择使用pip 下载的镜像源',
                               type=str,
                               metavar='类型',
                               choices=[
                                   "默认源",
                                   "清华大学",
                                   "阿里云",
                                   "中国科技大学",
                                   "豆瓣(douban)",
                                   "中国科技大学",
                                   "华中理工大学",
                                   "山东理工大学",

                               ],
                               default="默认源"
                               )


    # 阿里云 http://mirrors.aliyun.com/pypi/simple/
    # 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    # 豆瓣(douban) http://pypi.douban.com/simple/
    # 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    # 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

    # 清华：https://pypi.tuna.tsinghua.edu.cn/simple
    #
    # 阿里云：http://mirrors.aliyun.com/pypi/simple/
    #
    # 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    #
    # 华中理工大学：http://pypi.hustunique.com/
    #
    # 山东理工大学：http://pypi.sdutlinux.org/
    #
    # 豆瓣：http://pypi.douban.com/simple/
    # pip
    # install - i
    # https: // pypi.tuna.tsinghua.edu.cn / simple(要安装的包)

    # ===================================================================

    #adb shell
    adb_shell_parser = subs.add_parser(
        'adb_shell', help='adb 操作'
    )
    group1 = adb_shell_parser.add_argument_group('设备连接')
    group1.add_argument('-H', widget="TextField",
                        help='设备ip', type=str)
    group1.add_argument('-P', widget="TextField",
                        help='设备端口', type=str)


    # 接收界面传递的参数
    args = parser.parse_args()
    # print(args)
    # print(args.create)
    if args:
        if args.create == 1:
            print("已启动浏览器且已经为你打开了 fastTest 官方教程文档及官方网站")

        if args.create == "download" and args.package is not None:
            # print(args.package)
            os.system(f"pip3 install {args.package}")


        if args.create == "adb_shell":

            if args.H and args.P:
                HOST = f"{args.H}:{args.P}"
                os.system(f"adb connect {HOST}")
                print(HOST)



            # print(subprocess.Popen(k_shell, stdout=subprocess.PIPE).communicate()[0])






# if os.path.exists(filepath):
# 	os.mkdir(filepath + "\\%s" % val)
#
# else:
# 	print("不是文件夹")

# print(xt,name)
# os.mkdir()


# if args:
# 	os.system("start www.baidu.com")	print(1)


if __name__ == '__main__':
    main()

