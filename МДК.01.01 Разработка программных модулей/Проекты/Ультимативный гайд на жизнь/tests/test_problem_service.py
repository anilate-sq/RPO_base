# Тесты сериса проблем

import pytest
from unittest.mock import patch
from app.services.problem_service import resolve_problem, get_active_problems
from app.core.models import ProblemStatus, UserProblemHistory, Problem

@patch('app.services.problem_service.random.randint', return_value=50)
def test_resolve_problem_success(mock_rand, db_session, sample_user, sample_active_problem):
    problem, action = sample_active_problem
    result = resolve_problem(db_session, sample_user.id, problem.id, action.id)

    assert result["success"] is True
    assert result["xp_gained"] == 20
    assert result["stat_changed"]["balance"] == -300
    assert result["stat_changed"]["stress"] == 5

    # Проверка записи в историю
    history = db_session.query(UserProblemHistory).filter_by(problem_id=problem.id).first()
    assert history is not None
    assert history.was_successful is True

    # Проверка смены статуса
    problem = db_session.get(Problem, problem.id)
    assert problem.status == ProblemStatus.разрешенная

@patch('app.services.problem_service.random.randint', return_value = 90)
def test_resolve_problem_failure(mock_rand, db_session, sample_user, sample_active_problem):
    problem, action = sample_active_problem
    result = resolve_problem(db_session, sample_user.id, problem.id, action.id)

    assert result['success'] is False
    assert result['gained'] == 10
    assert result['stat_changes']['stress'] == 10

def test_resolve_invalid_problem(db_session, sample_user):
    with pytest.raises(ValueError, match="Проблема не найдена или уже решена"):
        resolve_problem(db_session, sample_user.id, problem_id=999, action_id=1)

def test_get_active_problems_only_active(db_session, sample_user, sample_active_problem):
    problem, action = sample_active_problem
    solved = Problem(user_id=sample_user.id, title="Решено", status=ProblemStatus.резрешенная)
    db_session.add(solved)
    db_session.commit()

    active_list = get_active_problems(db_session, sample_user.id)
    assert len(active_list) == 1
    assert active_list[0]["title"] == "Кушать хочется"