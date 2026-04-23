# Тестовый скрипт для подключения к базе данных

from app.core.database import get_db_session
from app.core.models import User, Section, Guide, Skill, Achievement
from app.services.user_service import get_user_profile, get_user_skills

def test_connection():
    try:
        with get_db_session() as db:
            users_count = db.query()
            print("Количество пользователей: ", users_count)

            users = db.query(User).all()
            for user in users:
                print(f'Польльзователь: {user.username}\n Уровень {user.level},\n  Баланс {user.balance},\n  Энергия {user.energy},\n  Стресс {user.stress_level}')

            sections_count = db.query(Section).count()
            print("Количество секций: ", sections_count)
            sections = db.query(Section).all()
            for section in sections:
                print(f'Секция: {section.title}({section.color})')

            guides_count = db.query(Guide).count()
            guides = db.query(Guide).all()
            for guide in guides:
                print(f'{guide.title} - {guide.status}, +{guide.xp_reward}XP')

            skills_count = db.query(Skill).count()
            print("Количество навыков: ", skills_count)

            achievements_count = db.query(Skill).count()
            print(f'Количество достижений: {achievements_count}')

            test_user = db.query(User).filter(User.username == "Студент 1").first()
            if test_user:
                profile = get_user_profile(db, test_user.id)
                print('Профиль существует')

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    test_connection()    