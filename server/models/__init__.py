import os
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text


# 讀取 .env
FILE_DIR= os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
with open(FILE_DIR) as f:
    for line in f:
        if line.startswith('#') or '=' not in line:
            continue
        key, value = line.strip().split('=', 1)
        os.environ[key] = value
        
DATABASE_USER_NAME= os.getenv("DB_USER")
DATABASE_PASSWORD= os.getenv("DB_PASSWORD")
DATABASE_NAME= os.getenv("DB_NAME_N")

# 初始化 SQLite 資料庫連線
DATABASE_URL = f"mysql+mysqlconnector://{DATABASE_USER_NAME}:{DATABASE_PASSWORD}@localhost:10330/{DATABASE_NAME}"
engine = create_engine(DATABASE_URL, echo= True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)
    
    # 測試連接
    with engine.connect() as connection:
        result = connection.execute(text("SELECT '測試OK' AS message"))
        for row in result:
            print(row)