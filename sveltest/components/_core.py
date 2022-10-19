#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from typing import Optional, Union, List, Dict


from faker import Faker
from sveltest.bin.conf import settings
from sveltest.support import LanguageException
from sveltest.components._api._main import VirtualData

from sveltest.components._api._email import SveltestEmail
from sveltest.support.common import ObjectDict




class Data(VirtualData):

    def __init__(self):
        super(Data,self).__init__(language=settings.DATA_MOCK_LANGUAGE)


class SvelteEmail(SveltestEmail):
    """
    内置自动化测试使用
    """

    def __init__(self):
        self.conf = ObjectDict(settings.EMAIL_CONFIG)
        super(SvelteEmail, self).__init__(user=self.conf.USERNAME,password=self.conf.PWD,host=self.conf.PORT)

    def test_send(self,attachments:Optional[List]=None):
        """

        :param attachments:
        :return:
        """
        # mail_title 标题 count 总用例数 tester 测试人员  case_run_startTime 开始运行时间 case_run_endTime 测试结束时间
        # case_run_time 运行时长 pass_count 测试通过  pass_rate 通过率 fail_count 失败用例  failure_rate 失败率
        # error_count 错误用例 error_rate 错误率 skip_count 跳过用例 skip_rate 跳过率
        jin = JinJaTemplate()
        z = jin.get_template("email_test_template01.html").render(mail_title="自动化测试", tester="测试工程师",
                                                                case_run_startTime="2022年", case_run_time="18点",case_run_endTime="1000",
                                                                count=100, pass_count=100, fail_count=100,pass_rate="100%",
                                                                error_count=100, skip_count=10, description="测试测试",
                                                                content_title="自动化测试执行结果报告",failure_rate="1%",error_rate="1%",skip_rate="1%")


        if settings.DEBUG is False:
            self.send(
                to=self.conf.LISTS,
                cc=self.conf.CC_LIST if self.conf.CC_LIST else None ,
                subject=self.conf.EMAIL_SUBJECT_PREFIX+self.conf.TITLE,
                bcc=self.conf.CC_LIST,
                contents=[str(z).replace("\n",'')],
                attachments=attachments,
            )

# NextTestRunner
class Email(SveltestEmail):
    """
    可单独使用的邮件API
    """
    def __init__(self,user:Optional[str],password:Optional[str],
                 host:Optional[str]="smtp.163.com",):
        super(Email, self).__init__(user=user,password=password,host=host)


from jinja2 import PackageLoader, Environment,FileSystemLoader


class JinJaTemplate:

    def __init__(self):
        # 创建一个包加载器对象
        self.env = Environment(loader=FileSystemLoader(os.path.join(Path(__file__).resolve().parent.parent,"bin\conf\html").replace("\\","/")))
        print(os.path.join(Path(__file__).resolve().parent.parent,"bin\conf\html"))

    def get_template(self,t:Optional[str]):
        """

        """
        return self.env.get_template(t)

# template = env.get_template('bast.html')  # 获取一个模板文件
# template.render(name='daxin', age=18)  # 渲染





if __name__ == '__main__':
    fp = r'F:\interfaceTestng\case\ocr\test_parameter_base64.py'
    from pathlib import Path
    # print(os.path.join(Path(__file__).resolve().parent.parent,"bin\conf\html").replace("\\","/"))

    j = JinJaTemplate()
    z = j.get_template("email_test_template01.html").render(html_title="自动化测试",tester="111",mail_title="自动化",
                                                            case_run_startTime="2022年",case_run_time="18点",case_run_endTime="666",
                                                            count=100,pass_count=100,fail_count=100,error_count=100,skip_count=10,description="测试测试",
                                                            content_title="自动化测试执行结果报告")


    # with open("test.html","w+",encoding="utf-8" ) as f:
    #     f.write(z)
    #     f.close()

    s = SvelteEmail()
    s.test_send()
