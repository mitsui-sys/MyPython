# DBとの直接的な接続の情報を定義
# １．database.pyと同じパスにonegai.dbというファイルを絶対パスで定義
# ２．SQLiteを利用して1.で定義した絶対パスにDBを構築
# ３．DB接続用インスタンスを生成
# ４．Baseオブジェクトを生成して、
# ５．そこにDBの情報を流し込む


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'onegai.db')
engine = create_engine('sqlite:///' + databese_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)