# -*- coding:utf8 -*-
__author__ = 'SmallS'

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

# 导入view，否则not found
import views



#db = SQLAlchemy()
# from Application.private.kvdb_module import KvdbStorage
#login_manager = LoginManager()
# 初始化kvdb
# kv = KvdbStorage()