# Сервисный слой — бизнес-логика приложения

from app.service.user_service import(
    get_user_by_id, get_user_by_username, create_user, update_user_state,
    get_user_profile, get_user_skills
)

from app.service.problem_service import (
    get_active_problem, resolve_problem, create_problem, get_problem_by_id
)

from app.service.guide_service import (
    update_progress, complete_guide, get_guides, get_progress
)

__all__ = [
    "get_user_by_id", "get_user_by_username", "create_user", "update_user_state",
    "get_user_profile", "get_user_skills", "get_active_problem", "resolve_problem",
    "create_problem", "get_problem_by_id", "update_progress", "complete_guide", "get_guides",
    "get_progress"
]