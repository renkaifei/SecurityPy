from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sqlite_url = "sqlite:///./app.db"
echo=True

DBEngine = create_engine(sqlite_url,connect_args={"check_same_thread": False},echo=echo)
DBSession = sessionmaker(autocommit=False, autoflush=True, bind=DBEngine)


