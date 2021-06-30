import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250),nullable=False)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250),nullable=False)
    lastname = Column(String(250),nullable=False) 

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer,primary_key=True)
    user_from_id = Column(Integer,ForeignKey('user.id'))
    user_to_id = Column(Integer,ForeignKey('user.id'))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_data = Column(String(250),nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer,ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id= Column(Integer, primary_key = True)
    user_owner = Column(Integer, ForeignKey('user.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250),nullable=False)
    post_owner = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e