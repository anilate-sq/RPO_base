# Подключение к БД

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from contextlib import contextmanager

from app.config import DATABASE_URL

Base = declarative_base() # Подгружаем базовый шаблон модели

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=3600,
    echo=True
)

# Сессия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db_session() -> Session:
    # Контекстный менеджер для работы с сессией БД

    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def init_db():
    # Инициализация базы данных
    from app.core.models import Base
    Base.metadata.create_all(bind=engine)