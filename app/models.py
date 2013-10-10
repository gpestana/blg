from app import db
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, Boolean

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    email = Column(String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name