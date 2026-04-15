# SQLAlchemy модели

from datetime import datetime, date
from sqlalchemy import(
    Column, String, Integer, Float, Text, DateTime, Date,
    Boolean, ForeignKey, Enum, JSON, Index, CheckConstraint
)
from sqlalchemy.dialects.postgresql from ARRAY
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func
import enum

from app.core.database import Base

# Enum на русском из дампа

class GuideStatus(enum.Enum):
    __tablename__ = "guide_status"
    черновик = "черновик"
    актуальный = "актуальный"
    архивный = "архивный"

class ProblemType(enum.Enum):
    __tablename__ = "promlem_type"
    срочная = "срочная" 
    регулярная = "регулярная" 
    длительная = "длительная"

class ProblemStatus(enum.Enum):
    __tablename__ = "problem_status"
    активная = "активная"
    разрешенная = "разрешенная"
    отозванная = "отозванная"

class SkillCategory(enum.Enum):
    __tablename__ = "skill_category"
    жизненные = "жизненные"
    профессиональные = "профессиональные"
    здоровье = "здоровье"
    социальные = "социальные"

# models

class User(Base):
    # Пользователи

    __tablename__ = "users"

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(45), unique=True, nullable=False, index=True)
    email = Column(String(245), unique=True, nullable=False)
    password_hash = Column(String(245), nullable=False)
    avatar_url = Column(String(500))
    level = Column(Integer, nullable=False, default=1)
    experience = Column(Integer, nullable=False, default=0)
    experience_to_next_level = Column(Integer, nullable=False, default=100)
    balance = Column(Float, nullable=False, default=0.0)
    energy = Column(Integer, nullable=False, default=100)
    stress_level = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    is_active = Column(Boolean, nullable=False, default=True)

    # Relationships
    problems = relationship("Problem", back_populates="user", cascade="all, delete-orphan")
    skills = relationship("UserSkill", back_populates="user", cascade="all, delete-orphan")
    achievements = relationship("UserAchievements", back_populates="user", cascade="add, delete-orphan")
    guide_progress = relationship("GuideProgress", back_populates="user", cascade="add, delete-orphan")
    problem_history = relationship("UserProblemHistory", back_populates="user", cascade="add, delete-orphan")
    authored_sections = relationship("Section", back_populates="author")
    authored_guides = relationship("Guide", back_populates="author")
    
    def __repr_(self):
        return f'<User {self.username} (lvl {self.level})>'
    
class Section(Base):
    # Разделы
    __tablename__ = "sections"

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(45), nullable=True)
    description = Column(Text)
    icon = Column(String(50))
    color = Column(String(7))
    sort_order = Column(Integer, nullable=False, default=0, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    author = Column(Integer, ForeignKey("users.id", ondelete="set null"))

    # Relationships
    guides = relationship("Guide", back_populates="section", cascade="all, delete-orphan")
    author = relationship("User", back_populates="authored_sections")

    def __repr__(self):
        return f'<Section {self.title}>'
    
class Guide(Base):
    # Гайды
    __tablename__ = "guides"

    # Columns
    id = Column(Integer, primary_key=True, autoincrement = True)
    section_id = Column(Integer, ForeignKey('section.id', ondelete='cascade'), nullable=False, index=True)
    title = Column(String(245), nullable=False)
    short_description = Column(String(500))
    content = Column(JSON, nullable=False)
    status = Column(
        Enum(GuideStatus, values_callable=lambda x: [e.value for e in x]),
        nullable=False,
        default=GuideStatus.черновик,
        index=True
    )
    read_time = Column(Integer)
    difficulty = Column(String(20))
    tags = Column(ARRAY(String))

    # Статистика
    views_count = Column(Integer, default=0)
    likes_count = Column(Integer, default=0)

    # Достижения
    xp_reward = Column(Integer, nullable=False, default=10)
    skill_points = Column(JSON)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    author = Column(Integer, ForeignKey('users.id', ondelete='set null'))

    # Relationships
    section = relationship('Section', back_populates='guides')
    author = relationship('User', back_populates='authored_guides')
    progress = relationship('GuideProgress', back_populates='guide', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Guide {self.title}>'
    
class Skill(Base):
    # Справочник навыков
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    description = Column(Text)
    category = Column(
        Enum(SkillCategory, values_callable=lambda x: [e.value for e in x]),
        nullable=False,
        index=True
    )
    icon = Column(String(50))
    max_level = Column(Integer, nullable=False, default=10)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    user_skills = relationship("UserSkill", back_populates="skill", cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Skill {self.name}>'
    
class UserSkills(Base):
    # Навыки пользователей
    __tablename__ = 'user_skills'

    # Column
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='cascade'), nullable=False, index=True)
    skill_id = Column(Integer, ForeignKey('skills.id', ondelete='cascade'), nullable=False, index=True)
    level = Column(Integer, nullable=False, default=1)
    experience = Column(Integer, nullable=False, default=0)
    experience_to_next_level = Column(Integer, nullable=False, default=100)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationship
    user = relationship("User", back_populates="skills")
    skill = relationship("Skill", back_populates="user_skills")

    __table_args__ = {
        Index('ix_user_skills_user_skill', 'user_id', 'skill_id', unique=True),
    }

    def __repr__(self):
        return f'<UserSkill {self.skill.name} - lvl {self.level}'