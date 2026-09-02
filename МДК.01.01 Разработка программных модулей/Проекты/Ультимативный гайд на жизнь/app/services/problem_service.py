"""
Сервис для работы с проблемами и действиями
"""
import random
from typing import Dict, List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from app.core.models import Problem, ActionOption, UserProblemHistory, ProblemStatus, ProblemType

# Получение активных проблем
def get_active_problems(db: Session, user_id: int, status_filter: str = "active") -> List[Dict]:
    status_map = {
        "active": ProblemStatus.активная,
        "resolved": ProblemStatus.разрешенная,
        "all": None
    }
    query = db.query(Problem).filter(Problem.user_id == user_id)

    target_status = status_map.get(status_filter)
    if target_status is not None:
        query = query.filter(Problem.status == target_status)
    
    if status_filter == "urgent":
        query = query.filter(Problem.priority >= 7)

    problems = query.order_by(Problem.priority.desc(), Problem.created_at.desc()).all()

    return [
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "priority": p.priority,
            "status": p.status.value,  # 🔧 Убрал hasattr, всегда .value
            "type": p.problem_type.value,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "actions": [{
                "id": a.id,
                "title": a.title,
                "success_chance": a.success_chance,
                "xp_reward": a.xp_reward,
                "balance_change": a.balance_change,
                "energy_change": a.energy_change,
                "stress_change": a.stress_change
            } for a in p.action_options]
        }
        for p in problems
    ]

# Получение проблемы по её id
def get_problem_by_id(db: Session, problem_id: int, user_id: int) -> Optional[Problem]:
    return (
        db.query(Problem)
        .filter(Problem.id == problem_id, Problem.user_id == user_id)
        .first()
    )

def resolve_problem(
    db: Session,
    user_id: int,
    problem_id: int,
    action_id: int
) -> Dict:
    problem = db.query(Problem).filter(
        Problem.id == problem_id, 
        Problem.user_id == user_id,
        Problem.status == ProblemStatus.активная
    ).first()
    
    if not problem:
        raise ValueError("Проблема не найдена или уже решена")
    
    action = db.query(ActionOption).filter(
        ActionOption.id == action_id,
        ActionOption.problem_id == problem_id
    ).first()
    
    if not action:
        raise ValueError("Выбрано неверное действие") 
    
    success = random.randint(1, 100) <= action.success_chance

    actual_stress = action.stress_change if success else max(0, action.stress_change + 5)
    actual_energy = action.energy_change
    actual_balance = action.balance_change
    actual_xp = action.xp_reward if success else max(1, action.xp_reward // 2)

    history = UserProblemHistory(
        user_id=user_id,
        problem_id=problem_id,
        action_id=action_id,
        was_successful=success,
        stress_change=actual_stress,
        energy_change=actual_energy,
        balance_change=actual_balance,
        xp_gained=actual_xp
    )
    db.add(history)

    problem.status = ProblemStatus.разрешенная
    problem.resolved_at = datetime.now()

    db.commit()

    return {
        "success": success,
        "xp_gained": actual_xp,
        "stat_changes": {
            "balance": float(actual_balance),
            "energy": int(actual_energy),
            "stress": int(actual_stress)
        },
        "problem_id": problem_id
    }

# Создание проблемы
def create_problem(
    db: Session, 
    user_id: int, 
    title: str, 
    description: str = "", 
    priority: int = 5, 
    p_type: str = "регулярная"
) -> Problem:
    try:
        problem_type_enum = ProblemType[p_type]
    except KeyError:
        problem_type_enum = ProblemType.регулярная
    
    problem = Problem(
        user_id=user_id,
        title=title,
        description=description,
        priority=max(1, min(10, priority)),
        problem_type=problem_type_enum
    )
    db.add(problem)
    db.commit()
    db.refresh(problem)
    return problem

def update_problem(
    db: Session,
    problem_id: int,
    user_id: int,
    title: str = None,
    description: str = None,
    priority: int = None,
    p_type: str = None
) -> Problem:
    """Обновить существующую проблему"""
    problem = db.query(Problem).filter(
        Problem.id == problem_id,
        Problem.user_id == user_id
    ).first()
    
    if not problem:
        raise ValueError("Проблема не найдена или у вас нет прав на её редактирование")
    
    if title is not None:
        problem.title = title.strip()
    if description is not None:
        problem.description = description.strip()
    if priority is not None:
        problem.priority = max(1, min(10, priority))
    if p_type is not None:
        try:
            problem.problem_type = ProblemType(p_type)
        except ValueError:
            pass  # Игнорируем неверные значения
    
    db.commit()
    db.refresh(problem)
    return problem


def delete_problem(db: Session, problem_id: int, user_id: int) -> bool:
    """Удалить проблему (только если она принадлежит пользователю)"""
    problem = db.query(Problem).filter(
        Problem.id == problem_id,
        Problem.user_id == user_id
    ).first()
    
    if not problem:
        raise ValueError("Проблема не найдена или у вас нет прав на её удаление")
    
    db.delete(problem)
    db.commit()
    return True