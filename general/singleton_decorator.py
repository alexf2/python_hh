import os
import threading

from logger import Logger


def singleton(cls):
    instances = {}
    lock = threading.Lock()

    def getinstance(*args, **kwargs):
        res = instances.get(cls, None)
        if res:
            return res
        with lock:
            if cls not in instances:
                instances[cls] = result = cls(*args, **kwargs)
            return result
    return getinstance


@singleton
class MyLogger(Logger):
    pass


log = MyLogger('Test', os.path.join(os.getcwd(), 'test.log'))
print(type(log))
log.info('Сообщение 1')

log2 = MyLogger('Test', os.path.join(os.getcwd(), 'test.log'))
log2.info('Сообщение 2')

print(log == log2)
