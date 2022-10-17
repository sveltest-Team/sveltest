
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


"""统一执行测试用例，并生成测试报告"""


import os
import time

from sveltest.bin.conf import settings

from typing import Dict,Optional

from sveltest.support.common import is_dir
from sveltest.components.htmlTestRunner import HTMLTestRunner
from sveltest.support.system import ZipFile

from sveltest.support.logger_v2 import log_v2
TEST_REPORT = {
    'context_processors':
        {
            'zip':'',
            'html':'',
            'img':'',
        }
}

get_case = getattr(settings, "CASE_SUITE_PATH")


# case_path = os.path.join(get_case,'case')
# guanfl
# v1.0.1
# 20210602
# :TODO :完成第一版 待单元测试
class MainTestSuite(object):
    """

    """
    def __init__(self,report_filename:Optional[str]=None):
        if report_filename is None:self.report_filename = "自动化测试报告"
        else:self.report_filename = report_filename

    #     服务启动
        if getattr(settings, "API_TEST_TEMPLATE") is True:
            pass

    def test_suite_base(self,suites:Optional[list],
                        test_title_name:Optional[str]=None,
                        description:Optional[str]=None,
                        thread_count:Optional[int]=0,
                        save_last_try:Optional[bool]=True,
                        ) -> Dict:
        """

        """

        # #测试报告保存的路径
        now = time.strftime('%Y-%m-%d', time.localtime())
        # get_html = getattr(settings, "TEST_REPORT")

        # 如果有配置html报告路径则进行使用配置里的数据、没有将进行使用tank默认的存放路径
        if not settings.TEST_REPORT:
            # get_base= getattr(settings, "BASE_DIR")
            path = os.path.join(settings.BASE_DIR,'report/html',now).replace('\\','/')
        else:
            path = os.path.join(settings.TEST_REPORT["HTML"],now).replace('\\','/')

        # 判断当 report_base 目录是否已存在、如果不存在就进行创建新的目录
        try:
            if os.path.exists(path):
                log_v2.info(path+"已存在，将跳过创建操作")
            else:
                log_v2.warning("测试结果输出存放的目录不存在，正在创建该目录")
                os.makedirs(path,exist_ok=True)
                log_v2.success(f"创建成功，创建的目录路径为："+path)
            # else:
            #     pass

        except Exception as e:
            log_v2.error(e)
        #
        #
        joinPath = os.path.join(path,'%s_%s.html'%(self.report_filename,now)).replace("\\","/")
        #
        fp = open(joinPath, 'wb')

        # 测试过程中的数据流写入到打开的报告中
        runner = HTMLTestRunner(
            stream=fp,
            retry=settings.TEST_CASE_ERROR_RETRY,
            title=test_title_name,
            description=description,
            save_last_try=save_last_try,
            verbosity=settings.LOGGING_VERBOSITY
        )
        #
        text_content = runner.run(suites,max_workers=thread_count)

        if not settings.TEST_REPORT and settings.TEST_REPORT["START_ZIP"] is True:

            if settings.TEST_REPORT["ZIP"]:
                get_base = getattr(settings, "BASE_DIR")
                zip_file_report_path = os.path.join(get_base, 'report/zip/%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")
                zip_path_save = ZipFile()
                path = zip_path_save.zip_file(path=path,zipfile_name=zip_file_report_path)
                log_v2.info("已对目录路径为：{},下的文件进行打包成zip文件,存放路径为：{}".format(path,zip_file_report_path))

        return  text_content


    # def test_suite_report_zip(self,suites,test_title_name=None,description=None):
    #     """
    #     可以将测试报告进行打包
    #     :param test_title_name:
    #     :param description:
    #     :return:
    #     """
    #     # get_case = getattr(settings, "CASE_SUITE_PATH")
    #
    #     # 定义测试执行器
    #     # suite = defaultTestLoader.discover(start_dir=get_case, pattern=getattr(settings, "TEST_CASE_ENFORCE_RULES"))
    #
    #     # #测试报告保存的路径
    #     now = time.strftime('%Y-%m-%d', time.localtime())
    #     get_html = getattr(settings, "TEST_REPORT")
    #
    #     # 如果有配置html报告路径则进行使用配置里的数据、没有将进行使用tank默认的存放路径
    #     if not get_html["context_processors"]:
    #         get_base = getattr(settings, "BASE_DIR")
    #         path = os.path.join(get_base, 'report/html', now).replace('\\', '/')
    #     else:
    #         path = os.path.join(get_html["context_processors"]["html"], now).replace('\\', '/')
    #
    #     # 判断当 report_base 目录是否已存在、如果不存在就进行创建新的目录
    #     try:
    #         if is_dir(path) is False:
    #             pass
    #         else:
    #             log4j.info(msg=f"正在创建{path}目录")
    #             os.mkdir(path)
    #     except Exception as e:
    #         log4j.error(msg=e)
    #     #
    #     #
    #     joinPath = os.path.join(path, '%s_%s.html' % (self.report_filename,now)).replace("\\", "/")
    #     #
    #     fp = open(joinPath, 'wb')
    #
    #     get_retry = getattr(settings, "TEST_CASE_ERROR_RETRY")
    #     # 测试过程中的数据流写入到打开的报告中
    #     runner = HTMLTestRunner(
    #         stream=fp, retry=get_retry, title=test_title_name,
    #         description=description, save_last_try=save_last_try, verbosity=3
    #     )
    #     #
    #     text_content = runner.run(suites)
    #
    #     # 进行对测试结果进行打包成一个zip压缩包
    #     log4j.info(msg="正在准备打包测试报告为zip,本次打包的目录路径为：{}".format(path))
    #     # 生成手写识别打包成zip文件的目录路径
    #
    #     if not get_html["context_processors"]:
    #         get_base = getattr(settings, "BASE_DIR")
    #         zip_file_report_path = os.path.join(get_base, 'report/zip/%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")
    #     else:
    #         zip_file_report_path = os.path.join(get_html["context_processors"]["zip"],
    #                                        '%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")
    #
    #     zip_path_save = ZipFile()
    #     path = zip_path_save.zip_file(path=path,zipfile_name=zip_file_report_path)
    #     log4j.info(msg="已对目录路径为：{},下的文件进行打包成zip文件,存放路径为：{}".format(path,zip_file_report_path))
    #
    #     return text_content


    # def test_suite_send_email(self,context,test_title_name=None,description=None,email_title=None,filename=None):
    #     """
    #     自动邮件
    #     :param test_title_name:
    #     :param description:
    #     :return:
    #     """
    #     get_case = getattr(settings, "CASE_SUITE_PATH")
    #
    #     # 定义测试执行器
    #     suite = defaultTestLoader.discover(start_dir=get_case, pattern=getattr(settings, "TEST_CASE_ENFORCE_RULES"))
    #
    #     # #测试报告保存的路径
    #     now = time.strftime('%Y-%m-%d', time.localtime())
    #     get_html = getattr(settings, "TEST_REPORT")
    #
    #     # 如果有配置html报告路径则进行使用配置里的数据、没有将进行使用tank默认的存放路径
    #     if not get_html["context_processors"]:
    #         get_base = getattr(settings, "BASE_DIR")
    #         path = os.path.join(get_base, 'report/html', now).replace('\\', '/')
    #     else:
    #         path = os.path.join(get_html["context_processors"]["html"], now).replace('\\', '/')
    #
    #     # 判断当 report_base 目录是否已存在、如果不存在就进行创建新的目录
    #     try:
    #         if is_dir(path) is False:
    #             pass
    #         else:
    #             log4j.info(msg=f"正在创建{path}目录")
    #             os.mkdir(path)
    #     except Exception as e:
    #         log4j.error(msg=e)
    #     #
    #     #
    #     joinPath = os.path.join(path, '%s_%s.html' % (self.report_filename,now)).replace("\\", "/")
    #     #
    #     fp = open(joinPath, 'wb')
    #
    #     get_retry = getattr(settings, "TEST_CASE_ERROR_RETRY")
    #     # 测试过程中的数据流写入到打开的报告中
    #     runner = HTMLTestRunner(
    #         stream=fp, retry=get_retry, title=test_title_name,
    #         description=description, save_last_try=True, verbosity=3
    #     )
    #     #
    #     text_content = runner.run(suite)
    #
    #     # 进行对测试结果进行打包成一个zip压缩包
    #     log4j.info(msg="正在准备打包测试报告为zip,本次打包的目录路径为：{}".format(path))
    #     # 生成手写识别打包成zip文件的目录路径
    #
    #     if not get_html["context_processors"]:
    #         get_base = getattr(settings, "BASE_DIR")
    #         zip_file_report_path = os.path.join(get_base, 'report/zip/%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")
    #     else:
    #         zip_file_report_path = os.path.join(get_html["context_processors"]["zip"],
    #                                        '%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")
    #
    #     zip_path_save = ZipFile()
    #     path = zip_path_save.zip_file(path=path,zipfile_name=zip_file_report_path)
    #     log4j.info(msg="已对目录路径为：{},下的文件进行打包成zip文件,存放路径为：{}".format(path,zip_file_report_path))
    #
    #     time.sleep(2)
    #     if email_title is None:title = "自动化测试报告"
    #     else:title = email_title
    #
    #     # 自动邮件发送
    #     get_bug =  getattr(settings, "DEBUG")
    #     get_email_list =  getattr(settings, "EMAIL_LISTS")
    #     try:
    #         if filename is None:fileName = "result.zip"
    #         else:fileName = filename
    #
    #         get_email_sender =  getattr(settings, "EMAIL_SENDER")
    #
    #         if get_bug is False:
    #             if not get_email_sender["context_processors"]:
    #                 log4j.debug(msg="你还没有进行配置EMAIL_SENDER,请配置 EMAIL_SENDER")
    #             else:
    #                 Email(sender=get_email_sender["context_processors"]["username"], password=get_email_sender["context_processors"]["password"],
    #                              toaddrs=get_email_list,
    #                              title=title, htmlPATH=zip_file_report_path, FILEname=fileName,
    #                              content=context)
    #     except Exception as e:
    #         log4j.error(e)
    #
    #     return  text_content
    #



# from fastTest import TextTestRunner,TestSuite,TestLoader
# class TestCommand:
#
#     def __init__(self,command, stream=None, descriptions=True, verbosity=1,
#                  failfast=False, buffer=False, resultclass=None, warnings=None,
#                  *, tb_locals=False,module=None):
#         self.suite = None
#         self.stream = stream
#
#         self.runner = TextTestRunner(stream=self.stream, descriptions=descriptions, verbosity=verbosity,
#                                 failfast=failfast, buffer=buffer, resultclass=resultclass, warnings=warnings,
#                                 tb_locals=tb_locals, module=module)
#
#
#     def add(self,classname):
#         self.suite =TestSuite()
#
#         self.suite.addTest(classname)
#
#     def addloaderclass(self,classname):
#         self.suite=TestSuite()
#         self.loader=TestLoader()
#         self.suite.addTest(self.loader.loadTestsFromTestCase(classname))
#
#     def addloadermodule(self,module):
#         if module:
#             self.module = __import__(module)
#         self.suite=TestSuite()
#         self.loader=TestLoader()
#         self.suite.addTest(self.loader.loadTestsFromModule(self.module))
#
#     def discover(self,start_dir):
#         # discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
#         self.suite = TestSuite()
#         self.loader = TestLoader()
#         return self.suite.addTest( self.loader.discover(start_dir=start_dir, pattern="*.py"))
#
#
#
#     def text_run(self):
#         self.runner.run(self.suite)
#
#
#     def html_run(self):
#         pass



#
# if __name__ == '__main__':
#
#     from fastTest.lib.unit.loader import defaultTestLoader
#
#     suite = defaultTestLoader.discover(r'F:\multiplex\src\multiplex\tests_case', pattern="test_*.py")
#
#     # #测试报告保存的路径
#     now = time.strftime('%Y-%m-%d', time.localtime())
#
#
#
#     fp = open(r"F:\multiplex\src\multiplex\tests_case\report\test.html", 'wb')
#
#     # 测试过程中的数据流写入到打开的报告中
#     runner = HTMLTestRunner(
#
#         stream=fp,  title=1,retry=2,
#         description=1,  verbosity=3
#     )
#
#     runner.run(suite)
#
