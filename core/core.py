from flask import Flask
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from setting import setting
from flask_script import Manager


mongodb = None
mysqldb = None


def create_app(**kwargs):
    def __init__():
        pass

    app = Flask(__name__)
    mg = kwargs.get('mongodb', False)
    my = kwargs.get('mysql', False)
    if mg:
        global mongodb
        app.config['MONGODB_SETTINGS'] = setting.mongodb
        mongodb = MongoEngine()
        mongodb.init_app(app)
    if my:
        global mysqldb
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+%s://%s:%s@%s:%d/%s' % tuple(setting.mysql.values())
        app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        mysqldb = SQLAlchemy(app)
        mysqldb.init_app(app)
    return app

app = create_app(**setting.init)
manager = Manager(app)

if __name__ == '__main__':
    create_app(mysql=True)


