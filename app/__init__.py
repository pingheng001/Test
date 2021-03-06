#coding=utf-8
from flask_mail import Mail
from flask import  Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_pagedown import PageDown                      #客户端 Markdown 到 HTML 的转换程序

bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
mail = Mail()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])             #导入配置
    config[config_name].init_app(app)                       #初始化

    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    pagedown.init_app(app)
    login_manager.init_app(app)
    
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    return app
