#coding=utf-8
'''
import unittest
import re
from flask import url_for
from app import create_app, db
from app.models import User, Role

class  FlaskClientTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        Role.insert_roles()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get(url_for('main.index'))
        self.assertTrue('Stranger' in response.get_data(as_text=True))

    def test_register_and_login(self):
        #注册新账户
        response = self.client.post(url_for('auth.register'), data={
            'email': 'test@163.com',
            'username': 'testname',
            'password': '123456',
            'password2': '123456'
        })
        self.assertTrue(response.status_code == 302)
        #使用新注册的账号登录
        response = self.client.post(url_for('auth.login'), data={
            'email': 'test@163.com',
            'password': '123456'
        }, follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue(re.search(b'Hello,\s+testname!', data))
        self.assertTrue(
            b'You have not confirmed your account yet' in response.data)
        #发送确认令牌
        user = User.query.filter_by(email='test@163.com').first()
        token = user.generate_confirmation_token()
        response = self.client.get(url_for('auth.confirm', token=token),
                                    follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('You have confirmed your accout, Thanks!' in data)
        #退出
        response = self.client.get(url_for('auth.logout'),
                                   follow_redirects=True)
        data = response.get_data(as_text=True)
        self.assertTrue('You have been logout!' in data)
'''