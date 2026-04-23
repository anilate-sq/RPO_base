# Тесты сервиса пользователей: создание, обновление статов, увеличение уровня
import pytest
from app.services.user_service import create_user, get_user_profile, update_user_state
from app.core.models import User

def test_create_user(db_session):
    user = create_user(db_session, 'новенький', 'new@test.com', 'hash_test')
    assert user.id is not None
    assert user.username == 'новенький'
    assert user.level == 1
    assert user.balance == 0.0

def test_get_user_profile(db_session, sample_user):
    profile = get_user_profile(db_session, sample_user.id)
    assert profile is not None
    assert profile['username'] == "test_student"
    assert "level" in profile
    assert "balance" in profile

def test_level_up_single(db_session, sample_user):
    update_user_state(db_session, sample_user.id, experience=100)
    user = db_session.get(User, sample_user.id)
    assert user.level == 2
    assert user.experience == 0
    assert user.experience_to_next_level == 120

def test_level_up_multiple(db_session, sample_user):
    update_user_state(db_session, sample_user.id, experience=250)
    user = db_session.get(User, sample_user.id)
    assert user.level == 3
    assert user.experience < user.experience_to_next_level

def test_clamp_energy_and_stress(db_session, sample_user):
    update_user_state(db_session, sample_user.id, energy=200, stress_level=300)
    user = db_session.get(User, sample_user.id)
    assert user.energy == 0
    assert user.stress_level == 100