from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import configs


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:123456@127.0.0.1:3306/coco_data'

# 加载配置文件
app.config.from_object(configs)
db = SQLAlchemy(app)

