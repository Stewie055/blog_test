#!/usr/bin/env python
# coding=utf-8
import os.path 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(BASE_DIR,'test.db')
