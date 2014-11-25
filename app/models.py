#!/usr/bin/env python
# coding=utf-8
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from app import app,db



class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80),unique=True)
    email = db.Column(db.String(120),unique=True)
    posts = db.relationship('Post',backref='author',lazy='dynamic')
    

    def __init__(self,username,email):
        self.username = username
        self.email = email
        

    def __repr__(self):
        return '<User %r>' %self.username

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    catagory_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('posts',lazy='dynamic'))
    
    def __init__(self,title,body,category,author_id,pub_date=None):
        self.title = title
        self.body =body 
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.author_id=author_id
        self.pub_date = pub_date
        self.category = category
        
    def __repr__(self):
        return '<Post %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


