#coding=utf-8
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.googlemail.com'      # 发送服务器名
    MAIL_PORT = 587                          # 端口
    MAIL_USE_TLS = True                      # 启用传输层安全协议
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') # 发送服务器用户名
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')          # 发送服务器密码
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'                                   #主题前缀
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'                  #邮件发送者
    FLASKY_ADMIN = '997696988@qq.com'                                         # 邮件接收者
    FLASKY_POSTS_PER_PAGE = 8                                                 #每一页显示的记录数量
    FLASKY_FOLLOWERS_PER_PAGE = 10
    FLASKY_COMMENTS_PER_PAGE = 3
    SQLALCHEMY_RECORD_QUERIES = True                                          #启用记录查询统计数字的功能
    FLASKY_DB_QUERY_TIMEOUT = 0.5                                             #缓慢查询的阈值
    SSL_DISABLE = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.googlemail.com'      # 发送服务器名
    MAIL_PORT = 587                          # 端口
    MAIL_USE_TLS = True                      # 启用传输层安全协议
    MAIL_USERNAME = 'pingheng002@gmail.com' or os.environ.get('MAIL_USERNAME') # 发送服务器用户名
    MAIL_PASSWORD = 'ping123456' or os.environ.get('MAIL_PASSWORD')          # 发送服务器密码
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    #程序出错时发送电子邮件
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls, 'MAIL_USERNAME', None) is not None:
            credentials = (cls.MAIL_USERNAME, cls.MAIL_PASSWORD)
            if getattr(cls, 'MAIL_USE_TLS', None):
                secure = ()
        mail_handler = SMTPHandler(
            mailhost=(cls.MAIL_SERVER, cls.MAIL_PORT),
            fromaddr=cls.FLASKY_MAIL_SENDER,
            toaddrs=[cls.FLASKY_ADMIN],
            subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + ' Application Error',
            credentials=credentials,
            secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE'))
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
        # handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)
        # 输出到 stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)


config = {
    'development':  DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'heroku': ProductionConfig,
    'default': DevelopmentConfig
}

