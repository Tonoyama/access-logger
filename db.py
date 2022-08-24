from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time

# 接続先DBの設定
DATABASE = 'sqlite:///user.sqlite3'

# DBの設定
Engine = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=False,
    connect_args={"check_same_thread": False}
)

# モデルのベースクラスを作成
Base = declarative_base()

# ユーザ管理のモデルのクラスを作成
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    entered_at = Column(DateTime, default=func.now())
    exited_at = Column(DateTime, default=func.now(), onupdate=func.now())

def create_database():
    Base.metadata.create_all(bind=Engine)

def create_session():
    return sessionmaker(bind=Engine)()

if __name__ == "__main__":
    create_database()