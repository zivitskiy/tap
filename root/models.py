from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgid = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String, nullable=True)
    balance = db.Column(db.Integer, default=0, nullable=False)
    isref = db.Column(db.Boolean, default=False)
    refcount = db.Column(db.Integer, default=0, nullable=False)


def initdb(app):
    with app.app_context():
        db.create_all()


def adduser(tgid, name):
    with db.session.begin(subtransactions=True):
        user = User.query.filter_by(tgid=tgid).first()
        if user is None:
            user = User(tgid=tgid, name=name)
            db.session.add(user)
            db.session.commit()
