# !/usr/bin/env python
# -*- coding:utf-8 -*-


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

from typing import Dict, Optional

from sveltest.support.common import is_dir
from sveltest.components.htmlTestRunner import HTMLTestRunner
from sveltest.support.system import ZipFile

from sveltest.support.logger_v2 import log_v2

TEST_REPORT = {
    'context_processors':
        {
            'zip': '',
            'html': '',
            'img': '',
        }
}

get_case = getattr(settings, "CASE_SUITE_PATH")


# case_path = os.path.join(get_case,'case')
# guanfl
# v1.0.1
# 20210602
# :TODO :完成第一版
class MainTestSuite(object):
    """

    """

    def __init__(self, report_filename: Optional[str] = None):
        if report_filename is None:
            self.report_filename = "自动化测试报告"
        else:
            self.report_filename = report_filename

        #     服务启动
        if getattr(settings, "API_TEST_TEMPLATE") is True:
            pass

    def test_suite_base(self, suites: Optional[list],
                        test_title_name: Optional[str] = None,
                        description: Optional[str] = None,
                        thread_count: Optional[int] = 0,
                        save_last_try: Optional[bool] = True,
                        ) -> Dict:
        """

        """

        # #测试报告保存的路径
        now = time.strftime('%Y-%m-%d', time.localtime())

        # 如果有配置html报告路径则进行使用配置里的数据、没有将进行使用tank默认的存放路径
        if not settings.TEST_REPORT:

            path = os.path.join(settings.BASE_DIR, 'report/html', now).replace('\\', '/')
        else:
            path = os.path.join(settings.TEST_REPORT["HTML"], now).replace('\\', '/')

        # 判断当 report_base 目录是否已存在、如果不存在就进行创建新的目录
        try:
            if os.path.exists(path):
                log_v2.info(path + "已存在，将跳过创建操作")
            else:
                log_v2.warning("测试结果输出存放的目录不存在，正在创建该目录")
                os.makedirs(path, exist_ok=True)
                log_v2.success(f"创建成功，创建的目录路径为：" + path)
            # else:
            #     pass

        except Exception as e:
            log_v2.error(e)
        #
        #
        joinPath = os.path.join(path, '%s_%s.html' % (self.report_filename, now)).replace("\\", "/")
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
        text_content = runner.run(suites, max_workers=thread_count)

        if settings.TEST_REPORT and settings.TEST_REPORT["START_ZIP"] is True:

            if settings.TEST_REPORT["ZIP"]:
                try:
                    log_v2.info(f"正在为你创建测试结果打包存放目录,{settings.TEST_REPORT['ZIP']}")
                    zip_file_report_path = os.path.join(settings.TEST_REPORT['ZIP'],
                                                        '%s_%s.zip' % (self.report_filename, now)).replace("\\", "/")

                    os.makedirs(settings.TEST_REPORT["ZIP"], exist_ok=True)
                    log_v2.success("创建目录成功")
                    zip_path_save = ZipFile()
                    path = zip_path_save.zip_file(path=path, zipfile_name=zip_file_report_path)
                    log_v2.info(
                        "已对目录路径为：{},下的文件进行打包成zip文件,存放路径为：{}".format(settings.TEST_REPORT["HTML"], zip_file_report_path))
                except Exception as e:
                    log_v2.error(e)

            if settings.EMAIL_CONFIG and settings.AUTO_SEND_EMAIL is True:
                log_v2.warning("已开启自动邮件发送")
                from NextTestRunner import nextEmail
                try:
                    nextEmail().send(
                        html_title="sveltest自动化测试",
                        tester=",".join(settings.TEST_REPORT['TESTER']) if settings.TEST_REPORT and
                                                                           settings.TEST_REPORT[
                                                                               'TESTER'] else "自动化测试工程师",
                        mail_title=test_title_name,
                        case_run_startTime=text_content[-1][9], case_run_time=text_content[-1][10],
                        case_run_endTime=text_content[-1][11], count=text_content[-1][0],
                        pass_count=text_content[-1][1],
                        fail_count=text_content[-1][2], error_count=text_content[-1][3], skip_count=text_content[-1][4],
                        description=description, content_title="自动化测试执行结果报告", failure_rate=text_content[-1][6],
                        pass_rate=text_content[-1][5],
                        skip_rate=text_content[-1][8],
                        error_rate=text_content[-1][7]
                    )
                except Exception as e:
                    log_v2.error(e)

        return text_content

