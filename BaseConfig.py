class BaseConfig():
    # 以下是我个人常用的配置类，仅做参考
    # Mysql 配置 pymysql
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Tt123@106.14.158.222:3306/pydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它
    # 以下配置不常用
    SQLALCHEMY_POOL_SIZE = 5  # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
    SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是 10
    SQLALCHEMY_MAX_OVERFLOW = 2  # 控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃
    SQLALCHEMY_POOL_RECYCLE = 2  # 动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话，Flask-SQLAlchemy 会自动地设置这个值为2小时
    # Mongo配置
    # MONGODB_PORT = 27017
    # MONGODB_HOST = "**.**.**"
    # MONGODB_DB = "dbName"
    # MONGODB_USERNAME = "dbuser"
    # MONGODB_PASSWORD = "dbpasswd"

    # MQ配置 rabbitmq
    # MQ_USER_NAME = 'name'
    # MQ_USER_PAWD = 'pwd'
    # MQ_URL = 'host'
    # MQ_HOST = 5672

    # 初始化app
    # app = Flask('dbclient')

    # 初始化mysqldb
    # app.config.from_object(BaseConfig)
    # 这里用我们的配置类去初始化mysql连接
    # db = SQLAlchemy(app)