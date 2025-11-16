import os
import threading

from logger import Logger


class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls in cls._instances:
            return cls._instances[cls]
        with cls._lock:
            cls._instances[cls] = result = super().__call__(*args, **kwargs)
            return result


class MyLoggerMeta(Logger, metaclass=SingletonMeta):
    pass


log = MyLoggerMeta('MyLoggerMeta', os.path.join(os.getcwd(), 'test.log'))
print(type(log))
log.info('Сообщение 1 ext')

log2 = MyLoggerMeta('MyLoggerMeta', os.path.join(os.getcwd(), 'test.log'))
log2.info('Сообщение 2 ext')

print(log == log2)
