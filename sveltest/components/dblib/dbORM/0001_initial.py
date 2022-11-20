# Generated by Django 3.2.6 on 2022-07-27 15:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('createTime', models.DateTimeField(auto_now_add=True, max_length=0, null=True, verbose_name='创建时间')),
                ('updateTime', models.DateTimeField(max_length=0, null=True, verbose_name='修改时间')),
                ('deleteTime', models.DateTimeField(max_length=0, null=True, verbose_name='删除时间')),
                ('status', models.IntegerField(default=1, null=True, verbose_name='邮件状态')),
                ('popService', models.CharField(max_length=20, null=True, verbose_name='POP')),
                ('smtpService', models.CharField(max_length=20, null=True, verbose_name='SMTP')),
                ('imapService', models.CharField(max_length=20, null=True, verbose_name='IMAP')),
                ('email_user', models.CharField(max_length=40, null=True, verbose_name='user')),
                ('pwd', models.CharField(max_length=40, null=True, verbose_name='pwd')),
                ('email_pwd', models.CharField(max_length=40, null=True, verbose_name='授权码')),
                ('service', models.CharField(max_length=20, null=True, verbose_name='服务商')),
                ('replyWith', models.CharField(max_length=100, null=True, verbose_name='回复模板标识语')),
                ('is_delete', models.IntegerField(default=0, null=True, verbose_name='删除状态')),
                ('is_show', models.IntegerField(default=0, null=True, verbose_name='显示状态')),
                ('type', models.IntegerField(default=0, null=True, verbose_name='配置类型')),
            ],
            options={
                'verbose_name': '邮件服务商配置',
                'verbose_name_plural': '邮件服务商配置',
                'db_table': 'email_sys_config',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='id')),
                ('nickname', models.CharField(max_length=20, null=True, verbose_name='昵称')),
                ('phone', models.CharField(max_length=11, verbose_name='电话')),
                ('role', models.CharField(default='MEMBER', max_length=10, null=True, verbose_name='用户角色')),
                ('createTime', models.DateTimeField(auto_now_add=True, max_length=0, null=True, verbose_name='创建时间')),
                ('updateTime', models.DateTimeField(max_length=0, null=True, verbose_name='修改时间')),
                ('deleteTime', models.DateTimeField(max_length=0, null=True, verbose_name='删除时间')),
                ('recentlyLoginSite', models.CharField(max_length=20, null=True, verbose_name='最近登录地点')),
                ('token', models.CharField(max_length=80, null=True, verbose_name='token')),
                ('ip', models.CharField(max_length=20, null=True, verbose_name='登录ip')),
                ('status', models.IntegerField(default=1, null=True, verbose_name='用户状态')),
                ('isDelete', models.IntegerField(default=0, null=True, verbose_name='删除状态')),
                ('isShow', models.IntegerField(default=0, null=True, verbose_name='显示状态')),
                ('create_by', models.CharField(max_length=20, null=True, verbose_name='创建人')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]