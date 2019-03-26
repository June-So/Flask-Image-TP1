from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    url = db.Column(db.String(255), nullable=False)

    def __init__(self, url):
        self.url = url


db.create_all()
