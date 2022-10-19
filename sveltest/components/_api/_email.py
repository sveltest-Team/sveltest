#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/9/26
import smtplib
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import yagmail
from typing import Optional,Union,Dict,List,NoReturn

from sveltest.support.logger_v2 import log_v2

class SveltestEmail:
    # user 代表用户名
    # password 代表邮箱密码
    # host 代表发信服务器
    # port 发信端口
    # smtp_ssl 使用ssl协议（默认为true）
    # encoding 编码方式（默认utf-8）

    def __init__(self,user:Optional[str],password:Optional[str],
                 host:Optional[str]="smtp.163.com",
                 ):
        """

        :param user:
        :param password:
        :param host:
        """
        self.svelte_email = yagmail.SMTP(user=user, password=password, host=host)

    def img(self,path:Optional[str]=None):
        return yagmail.inline(path)


    def send(self,to:Union[str,Dict[str,str],List]=None,
             cc:Union[str,Dict[str,str],List]=None,
             bcc:Union[str,Dict[str,str],List]=None,
             subject:Union[str,Dict[str,str]]=None,
             contents:Union[List,str]=None,
             preview_only:Optional[bool]=None,
             attachments:Optional[List]=None,
             prettify_html:Optional[bool]=True,
             headers:Optional[Dict]=None,
             ) -> NoReturn :
        """

        :param to:
        :param cc:
        :param bcc:
        :param subject:
        :param contents:
        :param preview_only:
        :param attachments:
        :param prettify_html:
        :param headers:
        :return:
        """

        # 发送邮件
        self.svelte_email.send(
            # to 收件人，如果一个收件人用字符串，多个收件人用列表即可
            to=to,
            # cc 抄送，含义和传统抄送一致，使用方法和to 参数一致
            cc=cc,
            # subject 邮件主题（也称为标题）
            subject=subject,
            # contents 邮件正文
            contents=contents,
            # 仅预览，可发送邮件但对方收不到
            preview_only=preview_only,
            # 头部信息，传递字典参数
            headers=headers,
            prettify_html=prettify_html,
            bcc=bcc,#密送，与抄送的区别是收件人看不到其他人的邮箱地址
            # attachments 附件，和收件人一致，如果一个附件用字符串，多个附件用列表
            attachments=attachments)

        # 记得关掉链接，避免浪费资源
        self.svelte_email.close()




class Mail:
    """邮件的封装
    Attributes:
    """
    def sender(self,sender,password,toaddrs,title,content=None):
        """发送的基本配置
        Args:
            sender:发送人的邮箱
            password:发送人的邮件授权码不是邮箱密码
            toaddrs:接收人的邮箱可以是多个，列表类型
            title:邮件的标题
            content:邮件的正文
        Returns:
            example:
        Raises:
        """
        log_v2.info("正在发送自动邮件...")

        try:
            self.sender = sender

            self.password = password

            self.toaddrs = toaddrs

            self.content = content

            self.textApart = MIMEText(self.content,"html", 'utf-8')
            self.m = MIMEMultipart()
        # 加上这个qq邮箱不会退邮箱
            self.m['Subject'] = title
            self.m['from'] = sender
        # 用于列表元素切割
            self.m['to'] = ",".join(self.toaddrs)
            self.m.attach(MIMEText(self.content, 'html', 'utf-8'))
            # message = MIMEText(mail_msg, 'html', 'utf-8')


        except Exception:
            log_v2.error("邮件配置信息有误请重新修改邮件配置后再重试发送邮件操作")

    def html(self,path,filename):
        """发送正文为HTML格式的邮件
        Args:
            path:html文件路径
            filename:文件名
        Returns:
            example:
        Raises:
        """
        filepath = path
        htmlApart = MIMEImage(open(filepath, 'rb').read(), filepath.split('.')[-1])
        htmlApart.add_header('Content-Disposition', 'attachment', filename=filename)
        self.m.attach(htmlApart)

        return htmlApart
    def universalFile(self,path,filename):
        """发送任意类型的邮件格式
        Args:
            path:文件路径
            filename:文件名称
        Returns:
            example:
        Raises:
        """
        pdfFile = path
        pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
        pdfApart.add_header('Content-Disposition', 'attachment', filename=filename)
        self.m.attach(pdfApart)

    def smtp(self,smtp='smtp.163.com'):
        """邮件发送
        Args:
            smtp:邮件的服务类型
        Returns:
            example:
        Raises:
        """
        try:
            server = smtplib.SMTP_SSL(smtp)
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.toaddrs, self.m.as_string())
            log_v2.info("邮件已发送成功")
            server.quit()
        except smtplib.SMTPException as e:
            log_v2.info(e)

class UnittestMail:
    """
        发送邮件的整个流程封装
    Attributes:
        url:传入的是一个接口地址
    """
    def __init__(self,sender,password,toaddrs,title,htmlPATH,FILEname,content=None):
        """
        Args:
            sender:
            password:
            toaddrs:
            title:
            htmlPATH:
            FILEname:
            content:
        Returns:
            example:
        Raises:
        """
        try:
            log_v2.info("本次邮件发送人用户名：%s，密码：******"%sender)
            log_v2.info("本次邮件接收人用户名：%s"%toaddrs)
            e = Mail()
            e.sender(sender=sender,password=password,toaddrs=toaddrs,title=title,content=content)
            log_v2.info("邮件主题为%s"%title)
            e.universalFile(htmlPATH,FILEname)
            log_v2.info("邮件正文为%s" % content)
            log_v2.info("邮件附件路径%s" % htmlPATH)
            e.smtp()
        except Exception as e:
            log_v2.error("请往框架配置文件中修改邮件配置信息,error -- %s"%e)





