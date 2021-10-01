# テーブルのカラム情報を定義するためのクラス
# テーブル操作を行う際のレコード生成もこのクラスを通して行う
# 今回は神社に対しての「お願い」を格納するためのテーブル
# カラム構成は
# ID（int：キー情報）
# title（String(128)：お願いのタイトル）
# body（text：お願いの内容）
# date（datetime：お願いの投稿日時）
from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class OnegaiContent(Base):
    __tablename__ = 'onegaicontents'
    id = Column(Integer, primary_key=True)
    title = Column(Text, unique=True)
    body = Column(Text)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, body=None, date=None):
        self.title = title
        self.body = body
        self.date = date

    def __repr__(self):
        return '<Title %r>' % (self.title)