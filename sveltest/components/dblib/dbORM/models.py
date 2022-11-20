#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2022/5/17
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=40, verbose_name='id')
    # username = models.CharField(max_length=20, verbose_name='用户名',unique=True)
    # USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = "username"
    nickname = models.CharField(null=True, max_length=20, verbose_name='昵称')
    phone = models.CharField(max_length=11, verbose_name='电话')
    role = models.CharField(null=True, max_length=10, verbose_name='用户角色', default="MEMBER")     # member MEMBER 普通会员
    createTime = models.DateTimeField(null=True, max_length=0, verbose_name='创建时间',auto_now_add=True,)
    updateTime = models.DateTimeField(null=True, max_length=0, verbose_name='修改时间')
    deleteTime = models.DateTimeField(null=True, max_length=0, verbose_name='删除时间')
    recentlyLoginSite = models.CharField(null=True, max_length=20, verbose_name='最近登录地点')
    token = models.CharField(null=True, max_length=80, verbose_name='token')
    ip = models.CharField(null=True, max_length=20, verbose_name='登录ip')
    status = models.IntegerField(null=True, default=1, verbose_name='用户状态')    # 1 正常 0被禁用	状态
    isDelete = models.IntegerField(null=True, default=0, verbose_name='删除状态')    # 1 为删除、0为未删除	逻辑删除标记
    isShow = models.IntegerField(null=True, default=0, verbose_name='显示状态')    # 	0 为显示、1为不显示	显示状态
    create_by = models.CharField(null=True, max_length=20, verbose_name='创建人')


    # 认证模型需要添加该属性
    # objects = UserManager()

    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return self.id

    class Meta:
        #   自定义表名
        db_table = 'user'
        # 表备注
        verbose_name_plural = "用户表"
        verbose_name = verbose_name_plural

class EmailConfig(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='id')
    createTime = models.DateTimeField(null=True, max_length=0, verbose_name='创建时间',auto_now_add=True,)
    updateTime = models.DateTimeField(null=True,  max_length=0, verbose_name='修改时间')
    deleteTime = models.DateTimeField(null=True, max_length=0, verbose_name='删除时间')
    # 0关闭 1 开启
    status = models.IntegerField(null=True, default=1, verbose_name='邮件状态')
    popService = models.CharField(null=True,max_length=20,verbose_name='POP')
    smtpService = models.CharField(null=True, max_length=20, verbose_name='SMTP')
    imapService = models.CharField(null=True,max_length=20, verbose_name='IMAP')
    email_user = models.CharField(null=True, max_length=40, verbose_name='user')
    pwd = models.CharField(null=True, max_length=40, verbose_name='pwd')
    email_pwd = models.CharField(null=True,max_length=40, verbose_name='授权码')
    service = models.CharField(null=True, max_length=20, verbose_name='服务商')
    replyWith = models.CharField(null=True,max_length=100, verbose_name='回复模板标识语')
    # # 1 正常 0被禁用	状态
    is_delete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
    # # 1 为删除、0为未删除	逻辑删除标记
    is_show = models.IntegerField(null=True, default=0, verbose_name='显示状态')

    # 0 邮件接收 1 邮件回复配置
    type = models.IntegerField(null=True, default=0, verbose_name='配置类型')

    def __str__(self):
          # 在该模型被关联是默认显示的字段
        return str(self.id)

    class Meta:
        #   自定义表名
        db_table = 'email_sys_config'
        # 表备注
        verbose_name_plural = "邮件服务商配置"
        verbose_name = verbose_name_plural
#
# class EmailReplyConfig(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name='id')
#     createTime = models.DateTimeField(null=True, max_length=0, verbose_name='创建时间',auto_now_add=True,)
#     updateTime = models.DateTimeField(null=True,  max_length=0, verbose_name='修改时间')
#     deleteTime = models.DateTimeField(null=True, max_length=0, verbose_name='删除时间')
#     status = models.IntegerField(null=True, default=1, verbose_name='邮件状态')
#     replyWith = models.CharField(null=True,max_length=100, verbose_name='回复模板标识语')
#     smtpService = models.CharField(null=True, max_length=20, verbose_name='SMTP')
#     email_user = models.CharField(null=True, max_length=40, verbose_name='user')
#     pwd = models.CharField(null=True, max_length=40, verbose_name='pwd')
#     email_pwd = models.CharField(null=True,max_length=40, verbose_name='授权码')
#     service = models.CharField(null=True, max_length=20, verbose_name='服务商')
#     # # 1 正常 0被禁用	状态
#     is_delete = models.IntegerField(null=True, default=0, verbose_name='删除状态')
#     # # 1 为删除、0为未删除	逻辑删除标记
#     is_show = models.IntegerField(null=True, default=0, verbose_name='显示状态')
#
#     def __str__(self):
#           # 在该模型被关联是默认显示的字段
#         return str(self.id)
#
#     class Meta:
#         #   自定义表名
#         db_table = 'email_reply_config'
#         # 表备注
#         verbose_name_plural = "邮件回复配置"
#         verbose_name = verbose_name_plural
#
#
