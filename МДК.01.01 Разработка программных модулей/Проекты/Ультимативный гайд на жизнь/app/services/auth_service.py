from typing import Optional
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.orm import Session
from app.core.models import User
from app.services.user_service import create_user as svc_create_user, get_user_by_username

ph = PasswordHasher() # Инициализация хешера для пароля
def hash_password(plain_password: str) -> str:
        return ph.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
        try:
                return ph.verify(hashed_password, plain_password)
        except VerifyMismatchError:
                return False
        
def register(db: Session, username: str, email: str, password: str) -> User:
        # Регистрация пользователя
        # Проверка уникальности
        if get_user_by_username(db, username):
                raise ValueError("Пользователь уже существует")
        if db.query(User).filter(User.email == email).first():
                raise ValueError("Email уже зарегестрирован")

def login(db: Session, username_or_email: str, password: str) -> Optional[User]:
        # Авторизация пользователя
        user = db.query(User).filter(username_or_email == User.username) | (User.email == username_or_email).first()

        if not user:
  
                  return None
        if verify_password(password, user.password):
              return user
        
        return None
