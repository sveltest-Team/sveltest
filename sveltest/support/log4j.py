#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/28


import logging.config

from sveltest.bin.conf import settings


standard_format = '%(levelname)s  %(asctime)s  %(threadName)s:%(thread)d_task_id:%(name)s_%(filename)s:%(lineno)d' \
                  ' msg:%(message)s'  # 其中name为getlogger指定的名字

simple_format = '%(levelname)s  %(asctime)s %(lineno)d' \
                ' msg:%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

logging_set_ = getattr(settings, "LOG_FILE_PATH")


LOGGING_CONFIG = {
    'version': 1,

    'disable_existing_loggers': False,
    # 定义日志 格式化的 工具
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'id_simple': {
            'format': id_simple_format
        },
    },
    # 过滤器
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'stream': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'standard'
        },
    },
    # logger实例
    'loggers': {
        # 默认的logger应用如下配置
        '_debug': {
            'handlers': ['stream'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}



class Log4J:
    """
    log日志封装
    Attributes:
    """
    def __init__(self):

        logging.config.dictConfig(LOGGING_CONFIG)
        self.logger = logging.getLogger("_debug")

    def info(self,msg):
        """用于打印出info级别的日志
        Args:
            msg:日志描述
        Returns:
            example:
        Raises:
        """
        self.logger.info(msg=msg)

    def debug(self,msg):
        """用于打印出debug级别的日志
        Args:
            msg:日志描述
        Returns:
            example:
        Raises:
        """
        self.logger.debug(msg=msg)

    def error(self,msg):
        """用于打印出error级别的日志
        Args:
            msg:日志描述
        Returns:
            example:
        Raises:
        """
        self.logger.error(msg=msg)

    def warning(self,msg):
        """用于打印出 warning 级别的日志
        Args:
            msg:日志描述
        Returns:
            example:
        Raises:
        """
        self.logger.warning(msg=msg)




