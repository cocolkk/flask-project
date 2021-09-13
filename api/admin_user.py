from flask import Flask, url_for, redirect
# import app
from app import app
from models.sys_user import SysUser





# @app.route('/login', methods=["get", "post"])
# def getUsers():
#     data = SysUser.get_data()
#     return dict(data=data)
