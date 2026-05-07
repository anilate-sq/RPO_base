# Сервис для работы с проблемами и действиями

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
            "status": p.status.value if hasattr(p.status, 'value') else p.status,
            "type": p.problem_type.value if hasattr(p.problem_type, 'value') else p.problem_type,
            "created_at": p.created_at.isoformat() if p.created_at else None,
            "actions": [{
                "id": a.id,
                "title": a.title,
                "success_chance": a.success_chance,
                "xp_reward": a.xp_reward,
                "balance_change": a.balance_change,
                "energy_change": a.energy_change,
                "stress_change": a.stress_change
            }
            for a in p.action_options
            ]
        }
        for p in problems
    ]

# Получение проблемы по её id
def get_problem_by_id(db, problem_id: int, user_id: int) -> Optional[Problem]:
    return(
        db.query(Problem)
        .filter(Problem.id == problem_id, Problem.user_id == user_id)
        .first()
    )

# Получение словаря решенных проблем
def resolve_problem(
        db: Session,
        user_id: int,
        problem_id: int,
        action_id: int
) -> Dict:
    problem = db.get(Problem, problem_id)
    if not problem or problem.user_id != user_id or problem.status != ProblemStatus.активная:
        raise ValueError("Проблемы отсутствуют или разрешены")
    
    action = db.get(ActionOption, action_id)
    if not action or action.problem_id != problem_id:
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
            "balance": actual_balance,
            "energy": actual_energy,
            "stress": actual_stress
        },
        "problem_id": problem_id
    }

# Создание проблемы
def create_problem(db, user_id: int, title: str, description: str = "", priority: int = 5, p_type: str = "регулярная") -> Problem:
    problem = Problem(
        user_id=user_id,
        title=title,
        description=description,
        priority=max(1, min(10, priority)),
        problem_type=ProblemType[p_type] if p_type in ProblemType.__members__ else ProblemType.регулярная       
    )
    db.add(problem)
    db.commit()
    db.refresh(problem)
    return problem