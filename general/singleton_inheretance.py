import os
import threading
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    VERBOSE = 1
    INFO = 2
    WARN = 3
    ERROR = 4


class SingletonBase:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if isinstance(cls._instance, cls):
            return cls._instance

        with cls._lock:
            cls._instance = super().__new__(cls)
            return cls._instance


class LoggerExt(SingletonBase):
    def __init__(self, name, file_path):
        self.name = name
        self.file_path = file_path

    def info(self, msg):
        self.log(LogLevel.INFO, msg)

    def warn(self, msg):
        self.log(LogLevel.WARN, msg)

    def error(self, msg):
        self.log(LogLevel.ERROR, msg)

    def log(self, level: LogLevel, msg: str):
        if msg:
            try:
                with open(self.file_path, 'a') as file:
                    file.write(
                        f'{datetime.now()}: {level.name}: {msg}{os.linesep}')
            except Exception as e:
                print(
                    f'Unexpected error at logging message "{msg}" of {level}: {e}')


log = LoggerExt('LoggerExt', os.path.join(os.getcwd(), 'test.log'))
print(type(log))
log.info('Сообщение 1 ext')

log2 = LoggerExt('LoggerExt', os.path.join(os.getcwd(), 'test.log'))
log2.info('Сообщение 2 ext')

print(log == log2)
