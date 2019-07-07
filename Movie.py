import datetime

from sqlalchemy import Column, Integer, String, UniqueConstraint, Index, DECIMAL, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

# 指定字符集、最大连接池数
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Tt123#@!@106.14.158.222:3306/pydb?charset=utf8", max_overflow=5)
# 先实例化sessionmaker类，Session对象加括号执行类下的__call__方法，
# 得到session对象，所以session可以调用Session类下的add，add_all等方法
Session = sessionmaker(bind=engine) # 指定引擎
session = Session()

Base = declarative_base()
# 创建单表
class Movie(Base):
    # 表名
    __tablename__ = 'py_douban_movie'
    # 表字段

    # 主键、默认自增
    id = Column(Integer,  primary_key=True, autoincrement=True)
    content_json = Column(String(2000))
    plat = Column(String(16))
    type = Column(Integer())
    title = Column(String(255))
    gmt_create = Column(DateTime())
    gmt_update = Column(DateTime())
    version = Column(Integer())
    ing = Column(String(255))
    image = Column(String(255))
    score = Column(DECIMAL(10,2))

    def __init__(self,content_json,plat,type,title,version,ing,image,score):
        self.content_json = content_json
        self.plat = plat
        self.type = type
        self.title = title
        self.gmt_create = datetime.datetime.now()
        self.gmt_update = datetime.datetime.now()
        self.version = version
        self.ing = ing
        self.image = image
        self.score = score

    # __table_args__ = (
    #     # UniqueConstraint('id', 'name', name='uix_id_name'),  # 唯一索引
    #     # 普通索引
    #     Index('idx_title', 'title', 'extra'),
    # )

    def __repr__(self):
        # 查是输出的内容格式，本质还是对象
        return "%s-%s" % (self.id, self.title)


def add_one_movie(movie):
    session.add(movie)
    session.commit()

def batch_add_movie(list):
    # session.add(movie)
    session.add_all(list)
    session.commit()

def delete(movie):
    session.query(movie.id).filter(movie.id > 2).delete()
    session.commit()

if __name__ == '__main__':
    movie = Movie("test","douban",1,"test",0,"test","http://www.google.com",92.5)
    movie2 = Movie("test2", "douban", 1, "test", 0, "test", "http://www.google.com", 92.5)
    list = []
    list.append(movie)
    list.append(movie2)
    # add_one_movie(movie)
    batch_add_movie(list)