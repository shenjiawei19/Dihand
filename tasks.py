from setting import logger

__all__ = ['task1', 'task2']


def task1(time=0.01, num=1, to=None):
    logger.getLogger("task1")
    print("my name is task1", time, num)



def task2(time=0.01, num=1):
    print("my name is task2", time, num)