from flask_script import Manager, Server
from app import app, db
from flask_migrate import Migrate, MigrateCommand
from models.sys_user import SysUser
from flask import request, jsonify
from collections import OrderedDict

manager = Manager(app)
Migrate(app=app, db=db)
manager.add_command('db', MigrateCommand)  # 创建数据库映射命令
manager.add_command('start', Server(port=5000, use_debugger=True))


@app.route('/')
def hello():
    data = SysUser.get_data()
    print(data)
    return "hello"


def user_to_dict(q):
    return OrderedDict(
        adminId=q.id,
        userName=q.user_name,
        account=q.account,
        password=q.password,
        phone=q.phone,
        email=q.mail,
        creatAt=q.create_time,
        status=q.status
    )


@app.route('/getUsers', methods=["get", "post"])
def getUsers():
    data = SysUser.get_data()
    # 把查询结果转换为json格式
    res = jsonify(list(map(user_to_dict, data)))
    return res


@app.route('/login', methods=['post'])
def login():
    req_data = request.get_json()
    username = req_data['userName']
    password = req_data['password']
    res = SysUser.get_user(username, password)
    print('****************')
    print('res---------->', res)
    if len(res) != 0:
        return "登录成功"
    elif len(res) == 0:
        return dict(status=401)



if __name__ == '__main__':
    manager.run()
