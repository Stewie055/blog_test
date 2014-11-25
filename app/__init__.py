#!/usr/bin/env python
# coding=utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'it is a key'
app.config.from_object('config')
db = SQLAlchemy(app)

from app import models,views
