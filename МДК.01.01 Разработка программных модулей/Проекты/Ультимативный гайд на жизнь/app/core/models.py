# SQLAlchemy модели

from datetime import datetime, date
from sqlalchemy import(
    Column, String, Integer, Float, Text, DateTime, Date,
    Boolean, ForeignKey, Enum, JSON, Index, CheckConstraint
)
from sqlalchemy.dialects.postgresql import ARRAY
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
    achievements = relationship("UserAchievement", back_populates="user", cascade="all, delete-orphan")
    guide_progress = relationship("GuideProgress", back_populates="user", cascade="all, delete-orphan")
    problem_history = relationship("UserProblemHistory", back_populates="user", cascade="all, delete-orphan")
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
    author_id = Column(Integer, ForeignKey("users.id", ondelete="set null"))

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
    section_id = Column(Integer, ForeignKey('sections.id', ondelete='cascade'), nullable=False, index=True)
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
    author_id = Column(Integer, ForeignKey('users.id', ondelete='set null'))

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
    
class UserSkill(Base):
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

    __table_args__ = (
        Index('ix_user_skills_user_skill', 'user_id', 'skill_id', unique=True),
    )

    def __repr__(self):
        return f'<UserSkill {self.skill.name} - lvl {self.level}'
    
class Problem(Base):
    # Проблемы случаются
    __tablename__ = "problems"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    problem_type = Column(
        Enum(ProblemType, values_callable=lambda x: [e.value for e in x]),
        nullable=False,
        default=ProblemType.регулярная,
        index=True
    )
    status = Column(
        Enum(ProblemStatus, values_callable=lambda x: [e.value for e in x]),
        nullable=False,
        default=ProblemStatus.активная,
        index=True
    )
    priority = Column(Integer, nullable=False, default=5)
    stress_impact = Column(Integer, default=10)
    energy_impact = Column(Integer, default=-5)
    balance_impact = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    resolved_at = Column(DateTime(timezone=True))

    # Отношения
    user = relationship("User", back_populates="problems")
    action_options = relationship("ActionOption", back_populates="problem", cascade="all, delete-orphan")
    history = relationship("UserProblemHistory", back_populates="problem", cascade="all, delete-orphan")
    
    __table_args__ = (
        CheckConstraint("priority >= 1 AND priority <= 10", name="check_priority_range"),
    )

    def __repr__(self):
        return f"<Problem {self.title} [{self.status}]>"
    
class ActionOption(Base):
    # Варианты действий для решения проблемы
    __tablename__ = "actions_options"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    problem_id = Column(Integer, ForeignKey("problems.id", ondelete="cascade"), nullable=False, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    balance_change = Column(Integer, default=0)
    stress_change = Column(Integer, default=0)
    energy_change = Column(Integer, default=0)
    xp_reward = Column(Integer, default=0)
    success_chance = Column(Integer, default=100)
    sort_order = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Отношения
    problem = relationship("Problem", back_populates="action_options")

    __table_args__ = (
        CheckConstraint("success_chance >= 0 AND success_chance <= 100", name="check_success_chance"),
    )

    def __repr__(self):
        return f'<ActionOption {self.title}>'
    
class UserProblemHistory(Base):
    # История разрешенных проблем
    __tablename__ = "user_problem_history"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False, index=True)
    problem_id = Column(Integer, ForeignKey("problems.id", ondelete="cascade"), nullable=False, index=True)
    action_id = Column(Integer, ForeignKey("actions_options.id", ondelete="restrict"), nullable=False)
    was_successful = Column(Boolean, nullable=False, default=True)
    stress_change = Column(Integer)
    energy_change = Column(Integer)
    balance_change = Column(Integer)
    xp_gained = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Отношения
    user = relationship("User", back_populates="problem_history")
    problem = relationship("Problem", back_populates="history")
    action = relationship("ActionOption")

    def __repr__(self):
        return f'<ProblemHistory {self.problem_id}>'
    
class GuideProgress(Base):
    # Прогресс чтения гайда
    __tablename__ = "guide_progress"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False, index=True)
    guide_id = Column(Integer, ForeignKey("guides.id", ondelete="cascade"), nullable=False, index=True)
    status = Column(String(20), nullable=False, default="не начато", index=True)
    progress_percent = Column(Integer, nullable=False, index=True)
    start_at = Column(DateTime(timezone=True), server_default=func.now())
    end_at = Column(DateTime(timezone=True))

    # Отношения
    user = relationship("User", back_populates="guide_progress")
    guide = relationship("Guide", back_populates="progress")

    __table_args__ = (
        Index("ix_guide_progress_user_guide", "user_id", "guide_id", unique=True),
        CheckConstraint("progress_percent >= 0 AND progress_percent <= 100", name="check_progress_percent")
    )

    def __repr__(self):
        return f"<GuideProgress {self.guide_id} - {self.progress_percent}>"
    
class Achievement(Base):
    # Достижения
    __tablename__ = "achievements"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    icon = Column(String(50))
    category = Column(String(50))
    condition_json = Column(JSON, nullable=False)
    xp_reward = Column(Integer, default=0)
    skill_points = Column(JSON)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Отношения
    user_achievements = relationship("UserAchievement", back_populates="achievement", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Achievement {self.name}>'
    
class UserAchievement(Base):
    # Достижения пользователя
    __tablename__ = "user_achievements"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False, index=True)
    achievement_id = Column(Integer, ForeignKey("achievements.id", ondelete="cascade"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Отношения
    user = relationship("User", back_populates="achievements")
    achievement = relationship("Achievement", back_populates="user_achievements")

    __table_args__ = (
        Index("ix_user_achievement_user_achievement", "achievement_id", unique=True),
    )

    def __repr__(self):
        return f'<UserAchievement {self.achievement.name}>'
    

class UserStats(Base):
    # Статистика пользователя
    __tablename__ = "user_stats"

    # Колонки
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="cascade"), nullable=False, unique=True, index=True)
    guides_read = Column(Integer, nullable=False, default=0)
    problem_solved = Column(Integer, nullable=False, default=0)
    days_active = Column(Integer, nullable=False, default=0)
    longest_streak = Column(Integer, nullable=False, default=0)
    current_streak = Column(Integer, nullable=False, default=0)
    last_activity_date = Column(Date, server_default=func.current_date())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Отношения
    user = relationship("User", backref="stats")

    def __repr__(self):
        return f'<UserStats user_id={self.users_id}>'