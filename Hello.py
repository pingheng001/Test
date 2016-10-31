#coding=utf-8
import os
from flask import Flask, render_template,url_for, session, redirect, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_script import Manager, Shell
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Message, Mail
from threading import Thread

app = Flask(__name__)

#basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SECRET_KEY'] = 'hard to guess string'
#配置Sqlite数据库
#app.config['SQLALCHEMY_DATABASE_URI'] = \
#    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#配置电子邮件
#app.config['MAIL_SERVER'] = 'smtp.googlemail.com'                       #发送服务器名
#app.config['MAIL_PORT'] = 587                                           #端口
#app.config['MAIL_USE_TLS'] = True                                       #启用传输层安全协议
#app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'                   #主题前缀
#app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'  #邮件发送者
#app.config['FLASKY_ADMIN'] = '997696988@qq.com'                         #邮件接收者
#app.config['MAIL_USERNAME'] = 'pingheng002@gmail.com'                   #发送服务器用户名
#app.config['MAIL_PASSWORD'] = 'ping123456'                              #发送服务器密码

#bootstrap = Bootstrap(app)
#moment = Moment(app)
manager = Manager(app)
#db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
#mail = Mail(app)

'''
app/email
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
'''
'''
manage
def make_shell_context():
    return dict(app=app, db=db, Role=Role, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
'''
'''
#mian/forms
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
'''
'''
#app/models
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
'''
'''
#main/views
@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_mail(app.config['FLASKY_ADMIN'], 'New User',
                          'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html',
                           form = form, name = session.get('name'), known=session.get('known', False))

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name = username)
'''
'''
#移到main/errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
'''

if __name__ == '__main__':
    db.create_all()
    manager.run()