from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# 替换为你的数据库连接信息
DATABASE_URL = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 初次建表时执行一次
def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
