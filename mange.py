# -*-coding:utf-8 -*-
# from flask_script import Manager
from core import manager
from core.task_manage import get_tasks
import importlib


@manager.command
def view():
    """
    Runs to list tasks
    """
    print(get_tasks())


@manager.option("-p", "--apps", dest="apps", help="app name.")
@manager.option("-t", "--tasks", dest="tasks", nargs="*", required="False", help="tasks name.")
@manager.option("-s", "-time", dest="time", default=0.01, help="Execute for sleep time.")
@manager.option("-n", "-num", dest="num", default=1, help="Execute for num")
def run(apps, tasks, num=None, time=None):
    """
    Runs to execute task if you need
    """
    app_task = 'apps.%s.tasks' % (apps)
    tasks_module = importlib.import_module(app_task)
    for t in tasks:
        task = getattr(tasks_module, t)
        task(t=time, num=num)

if __name__ == '__main__':
    manager.run()

