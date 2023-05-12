"""
    @logger 日志系统
    @file logger.py
    @name huanglewei
"""
import logging
import inspect
import colorlog


class Logger:
    def __init__(self, name=__name__, level=logging.DEBUG, log_file=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # 添加一个 StreamHandler 处理器，用于输出到控制台
        console_handler = logging.StreamHandler()

        console_formatter = colorlog.ColoredFormatter(
            '%(log_color)s%(levelname)s:   %(asctime)s   %(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            },
            reset=True,
            style='%'
        )


        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

        if log_file:
            handler = logging.FileHandler(log_file, encoding='utf-8')
        else:
            handler = logging.StreamHandler()


        # 输出日志到文件
        handler.setLevel(level)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # 输出日志到控制台
        console_handler.setLevel(level)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        frame = inspect.currentframe().f_back
        filename = inspect.getframeinfo(frame).filename
        lineno = inspect.getframeinfo(frame).lineno

        self.logger.info(f"{filename}[line: {lineno}] - {message}")

    def error(self, message):
        frame = inspect.currentframe().f_back
        filename = inspect.getframeinfo(frame).filename
        lineno = inspect.getframeinfo(frame).lineno

        self.logger.error(f"{filename}[line: {lineno}] -  {message}")

    def warn(self, message):
        frame = inspect.currentframe().f_back
        filename = inspect.getframeinfo(frame).filename
        lineno = inspect.getframeinfo(frame).lineno

        self.logger.warning(f"{filename}[line: {lineno}] -  {message}")

    def debug(self, message):
        print("debug"+message)
        frame = inspect.currentframe().f_back
        filename = inspect.getframeinfo(frame).filename
        lineno = inspect.getframeinfo(frame).lineno

        self.logger.debug(f"{filename}[line: {lineno}] - {message}")

    def debug_sql(self, message):

        self.logger.debug(f"debug_sql - {message}")



log = Logger(level=logging.DEBUG, log_file="app.log")
