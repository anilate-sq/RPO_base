# Сервис для работы с гайдами и прогрессом

from typing import Dict, List, Optional
from sqlalchemy.orm import Session
from app.core.models import Guide, GuideProgress, UserSkill, Skill
from app.services import user_service

# Получение актуальных гайдов 
def get_guides(db: Session, section_id: Optional[int] = None) -> List[Dict]:
    query = db.query(Guide).filter(Guide.status == "актуальный")
    if section_id:
        query = query.filter(Guide.section_id == section_id)
    guides = query.all()
    return[
        {
            "id": g.id,
            "title": g.title,
            "section_id": g.section_id,
            "short_description": g.short_description,
            "read_time": g.read_time,
            "difficulty": g.difficulty,
            "xp_reward": g.xp_reward,
            "tags": g.tags or []
        }
        for g in guides
    ]

# Получение прогресса пользователя по гайду
def get_progress(db, user_id: int, guide_id) -> Optional[Dict]:
    progress = db.query(GuideProgress).filter_by(user_id=user_id, guide_id=guide_id).first()
    if not progress:
        return None
    return{
        "guide_id": progress.guide_id,
        "status": progress.status,
        "progress_percent": progress.progress_percent,
        "end_at": progress.end_at.isoformat() if progress.end_at else None
    }
# Обновление прогресса
def update_progress(db: Session, user_id: int, guide_id: int, percent: int) -> GuideProgress:
    progress = db.query(GuideProgress).filter_by(user_id=user_id, guide_id=guide_id).first()
    if not progress:
        progress = GuideProgress(user_id=user_id, guide_id=guide_id, status="в процессе")
        db.add(progress)

    progress.progress_percent = max(0, min(100, percent))
    progress.status = "завершено" if percent >= 100 else "в процессе"
    if percent >= 100 and not progress.end_at:
        from datetime import datetime
        progress.end_at = datetime.now()

    db.commit()
    db.refresh(progress)
    return progress

# Пройденные гайды
def complete_guide(db: Session, user_id: int, guide_id: int) -> Dict:
    guide = db.get(Guide, guide_id)
    progress = db.query(GuideProgress).filter_by(user_id=user_id, guide_id=guide_id).first()
    if not guide or not progress or progress.progress_percent < 100:
        raise ValueError("Гайд не завершен")
    
    if progress.status == "награда получена":
        return {"rewarded": False, "message": "Награда уже получена"}
    
    user_service.update_user_state(db, user_id, experience=guide.xp_reward)

    skill_rewards = []
    if guide.skill_points:
        for skill_name, xp in guide.skill_points.items():
            skill = db.query(Skill).filter(Skill.name == skill_name).first()
            if not skill:
                continue
            us = db.query(UserSkill).filter_by(user_id=user_id, skill_id=skill.id).first()
            if not us:
                us = UserSkill(user_id=user_id, skill_id=skill.id)
                db.add(us)
                db.flush()

            us.experience += xp
            while us.experience >= us.experience_to_next_level:
                us.experience -= us.experience_to_next_level
                us.level += 1
                us.experience_to_next_level = int(us.experience_to_next_level * 1.2)
            skill_rewards.append({"name": skill_name, "xp": xp})

    progress.status = "награда_получена"
    db.commit()

    return{
        "rewarded": True,
        "xp_earned": guide.xp_reward,
        "skill_updated": skill_rewards
    }