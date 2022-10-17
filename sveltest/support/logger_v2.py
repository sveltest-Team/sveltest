#!/usr/bin/env python
#-*- coding:utf-8 -*-


import sys
from loguru import logger



class Log4j:
    def __init__(self, level: str = "DEBUG", colorlog: bool = True):
        self.logger = logger
        self._colorlog = colorlog
        self._console_format = "[ {level} ] - <green>{time:YYYY-MM-DD HH:mm:ss}</> - {file}:{line} - <level>{message}</level>"

        self._log_format = "{time: YYYY-MM-DD HH:mm:ss} {file}  {level}  {message}"
        self._level = level
        self.level(self._colorlog, self._console_format, self._level)

    def level(self, colorlog: bool = True, format: str = None, level: str = "DEBUG",path=None):
        if format is None:
            format = self._console_format
        self.logger.remove()
        self.logger.add(sys.stderr, level=level, colorize=colorlog, format=self._console_format)
        if path:
            self.logger.add(path, level=level, colorize=False, format=self._console_format, encoding="utf-8")


# log level: TRACE < DEBUG < INFO < SUCCESS < WARNING < ERROR
log_cfg = Log4j(level="TRACE")
log_v2 = logger







