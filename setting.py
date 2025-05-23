
import os

class Setting(object):
    EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")  # 发送邮件的邮箱
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
   
    DB = {
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USERNAME': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'DBNAME': 'login-register'
    }
    URI = f"mysql+pymysql://{DB['USERNAME']}:{DB['PASSWORD']}@{DB['HOST']}:{DB['PORT']}/{DB['DBNAME']}"
    SQLALCHEMY_DATABASE_URI = URI
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 自动提交数据处理
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 自动更跟踪数据库，性能不好
    SQLALCHEMY_POOL_SIZE = 10  # 连接数，默认5
    SQLALCHEMY_MAX_OVERFLOW = 20  # 超出连接数时，允许再新建的连接数,但是这5个人时不使用时，直接回收，默认10
    SQLALCHEMY_POOL_TIMEOUT = 30  # 等待可用连接时间，超时则报错，默认为30秒
    SQLALCHEMY_POOL_RECYCLE = 3600  # 连接生存时长（秒），超过则该连接被回收，再生存新连接,默认-1不回收连接
    SQLALCHEMY_POOL_PRE_PING = True  # 连接池的“预ping”，在每次签出时测试连接的活动性,若出现disconnect错误，该连接将立即被回收

    SQLALCHEMY_ECHO = False  # 显示原始SQL语句
    SQLALCHEMY_ECHO_POOL = False  # 连接池记录信息


class DevelopConfig(Setting):
    """开发环境"""
    # Database
    SQLALCHEMY_ECHO = True  # 显示原始SQL语句
    SQLALCHEMY_ECHO_POOL = True  # 连接池记录信息

    ENCRYPTION_KEY = "Pg^.l!8UdJ+Y7dMIe&fl*%!p9@ej]/#tL~3E4%6?"  # 加密密钥
    OBFUSCATION_START_TOKEN = "$^*ENCRYPT="  # 加密密钥的开头
    OBFUSCATION_END_TOKEN = "?&#$"  # 加密密钥的结尾


# 环境映射关系
mapping = {
    'develop': DevelopConfig,
}

CONFIG = mapping[os.environ.get('APP_ENV', 'develop').lower()]()  # 获取指定的环境
