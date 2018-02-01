import logging

fmt = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %X')
logger = logging.getLogger("task")
task = logging.FileHandler(r"E:/project/Dihand/log/task.log")
task.setFormatter(fmt=fmt)
logger.addHandler(hdlr=task)

logger.info("https://xml2.txodds.com/feed/odds/apmarkets.php?ident=huanhuba&passwd=7898789获取成功")
