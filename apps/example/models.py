from core.core import mongodb as mdb
from core.core import mysqldb as db


class User(mdb.Document):
    """
    update: test = User.objects(name=name,address=address)
    User(name=name , address=address).save()
    """
    email = mdb.StringField(required=True)
    first_name = mdb.StringField(max_length=50)
    last_name = mdb.StringField(max_length=50)


class User2(db.Model):
    """
    test = User2(uid=1, uname='test')
    db.create_all()
    db.session.add(test)
    db.session.commit()
    """
    __tablename__ = 'user'
    uid = db.Column(db.String(11), primary_key=True)
    uname = db.Column(db.String(11), unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.uname



