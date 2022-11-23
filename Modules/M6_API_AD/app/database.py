import sqlalchemy as sql
import sqlalchemy.orm as orm

# URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# ENGINE
engine = sql.create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SESSION
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# BASE
Base = orm.declarative_base()

