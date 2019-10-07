import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect #导入csrf保护
from flask_migrate import Migrate

from flask_restful import Api

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.config.from_object("settings.Config") #来源于类对象
app.secret_key = "123123"

models = SQLAlchemy(app)
#csrf = CSRFProtect(app) #使用csrf保护
api = Api(app)
migrate = Migrate(app,models) #安装数据库管理插件



