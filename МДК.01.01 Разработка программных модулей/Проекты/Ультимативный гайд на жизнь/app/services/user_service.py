"""
Сервис для работы с пользователями
"""
from typing import Optional, List
from sqlalchemy.orm import Session
from app.core.models import User, UserStats, UserSkill, Skill  # ← добавил Skill

# Получение данных пользователя по id
def get_user_by_id(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).get(user_id)

# Получение данных пользователя по его логину
def get_user_by_username(db: Session, username: str) -> Optional[User]:
    return db.query(User).filter(User.username == username).first()

# Добавление пользователя
def create_user(db: Session, username: str, email: str, password_hash: str) -> User:
    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
    )
    db.add(user)
    db.flush()  # Получаем user.id, но пока не коммитим

    stats = UserStats(user_id=user.id)
    db.add(stats)

    # Один атомарный коммит для всей операции
    db.commit()
    db.refresh(user)
    return user

# Обновление статистики
def update_user_state(
    db: Session,
    user_id: int,
    balance: float = None,
    energy: int = None,
    stress_level: int = None,
    experience: int = None
) -> User:
    user = get_user_by_id(db, user_id)
    
    if not user:
        raise ValueError(f"Пользователь {user_id} не найден")
    
    if balance is not None:
        user.balance += balance
    
    if energy is not None:
        user.energy = max(0, min(100, user.energy + energy))

    if stress_level is not None:
        user.stress_level = max(0, min(100, user.stress_level + stress_level))

    if experience is not None:
        user.experience += experience
        while user.experience >= user.experience_to_next_level:
            user.experience -= user.experience_to_next_level
            user.level += 1
            user.experience_to_next_level = int(user.experience_to_next_level * 1.2)

    db.commit()
    db.refresh(user)
    return user

# Получить данные профиля пользователя
def get_user_profile(db: Session, user_id: int) -> Optional[dict]:
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    
    return {
        "id": user.id,
        "username": user.username,
        "level": user.level,
        "experience": user.experience,
        "experience_to_next_level": user.experience_to_next_level,
        "balance": user.balance,
        "energy": user.energy,
        "stress_level": user.stress_level,
        "is_active": user.is_active
    }

# def get_user_role(db, user_id: int) -> Optional[dict]:
#     ...

# Получить навыки пользователя
def get_user_skills(db: Session, user_id: int) -> List[dict]:
    user_skills = db.query(UserSkill).filter(UserSkill.user_id == user_id).all()

    return [
        {
            "id": us.id,
            "skill_id": us.skill_id,
            "name": us.skill.name,  # ← было us.name
            "category": us.skill.category.value,  # ← было .category.values
            "icon": us.skill.icon,
            "level": us.level,
            "experience": us.experience,
            "experience_to_next_level": us.experience_to_next_level,
            "progress_percent": round((us.experience / max(us.experience_to_next_level, 1)) * 100, 2)
        }
        for us in user_skills
    ]