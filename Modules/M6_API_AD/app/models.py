import sqlalchemy as sql
import sqlalchemy.orm as orm

from database import Base

import datetime as dt

class User(Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    hashed_password = sql.Column(sql.String)
    is_active = sql.Column(sql.Boolean, default=True)

    posts = orm.relationship("Article", back_populates="owner")


class Article(Base):
    __tablename__ = "articles"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    title = sql.Column(sql.String, index=True)
    content = sql.Column(sql.String, index=True)
    owner_id = sql.Column(sql.String, sql.ForeignKey("users.id"))
    date_created = sql.Column(sql.DateTime, default=dt.datetime.utcnow)
    date_last_updated = sql.Column(sql.DateTime, default=dt.datetime.utcnow)

    owner = orm.relationship("User", back_populates="posts")

