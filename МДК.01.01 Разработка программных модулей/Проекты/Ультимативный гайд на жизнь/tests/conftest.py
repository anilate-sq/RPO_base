# Фикстуры для тестов
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.models import(
    Base, User, UserStats, Problem, ActionOption,
    UserProblemHistory, ProblemStatus, ProblemType
)

# Создание чистой БД в памяти для тестов
@pytest.fixture
def db_session():
    engine = create_engine('sqlite://memory', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    engine.dispose()

# Создание пользователей с привязкой статистики
@pytest.fixture
def sample_user(db_session):
    user = User(username="test_student", email="test@test.com", password_hash="test_hash")
    db_session.add(user)
    db_session.flush()
    stats = UserStats(user_id=user.id)
    db_session.add(stats)
    db_session.commit()
    db_session.refresh(user)
    return user

# Создание фикстуры для активной проблемы с единственным вариантом действия
@pytest.fixture
def sample_active_problem(db_session, sample_user):
    problem = Problem(
        user_id=sample_user.id,
        title="Кушать хочется",
        description="Тараканы в холодильнике",
        problem_type=ProblemType.срочная,
        status=ProblemStatus.активная,
        priority=9
    )
    db_session.add(problem)
    db_session.flush()
    
    action = ActionOption(
        problem_id=problem.id,
        title="Приготовить самому",
        success_chance=70,
        xp_reward=20,
        balance_change=-300,
        energy_change=-40,
        stress_change=5
    )
    db_session.add(action)
    db_session.commit()
    db_session.refresh(problem)
    return problem, action
