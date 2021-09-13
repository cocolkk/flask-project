from app import db
from flask import request


class SysUser(db.Model):
    __tablename__ = "admin_user"
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(64))
    password = db.Column(db.String(64))
    user_name = db.Column(db.String(64))
    phone = db.Column(db.String(64))
    mail = db.Column(db.String(64))
    status = db.Column(db.Integer)
    create_time = db.Column(db.String(64))

    # def __init__(self, id_, account, password, user_name,
    #              phone, mail, status, create_time):
    #     self.id_ = id_
    #     self.account = account
    #     self.password = password
    #     self.user_name = user_name
    #     self.phone = phone
    #     self.mail = mail
    #     self.status = status
    #     self.create_time = create_time

    @classmethod
    def add(cls):
        pass
        # new_user = SysUser(id_='', account='No2', password='123',
        #                             user_name='Wang', mail='lkkcocosdy@163.com',
        #                             create_time='', phone='13126896097', status=1)
        # db.session.add(new_user)
        # db.session.commit()

    @classmethod
    def get_data(cls):
        sql = "select * from admin_user"
        result = db.session.execute(sql).fetchall()
        print('result---->', result)
        return result

    @classmethod
    def get_user(cls, username, password):
        sql = "select * from admin_user where user_name ='%s' and password='%s' " % (username, password)
        res = db.session.execute(sql).fetchall()
        print('res0000000000', res)
        return res


# q = SysUser()
# q.get_data()






