#!/usr/bin/env python
# coding=utf-8
from app import app
from flask import render_template,flash,request

from .models import Post,User

@app.route('/')
def index():
    posts = Post.query.all()
    if posts:
        return render_template('index.html',posts=posts)

    else:
        flash('Oops,it seems there is no post now')
        return render_template('index.html',flash=flash)

@app.route('/user/',methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'dd':
            return "logged in"
        else:
            error = 'Invalid username or password'
    return render_template('login.html',error=error)

@app.route('/user/<username>/')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        pass
    else:
        message = 'cant find the user:'+username
        flash(message,category='message') 
    return render_template('user.html',user=user)
