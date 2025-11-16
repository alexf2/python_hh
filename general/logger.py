import os
from datetime import datetime
from enum import Enum


class LogLevel(Enum):
    VERBOSE = 1
    INFO = 2
    WARN = 3
    ERROR = 4


class Logger:
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
                        f'{datetime.now()}: {self.name}: {level.name}: {msg}{os.linesep}')
            except Exception as e:
                print(
                    f'Unexpected error at logging message "{msg}" of {level}: {e}')
