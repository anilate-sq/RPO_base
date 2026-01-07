from functools import wraps

# Сделаем декоратор для проверки роли пользователя в системе
def required_access(role):
    def decorator(func):
        @wraps(func) # Сохраняем методанные сохраняемое функции
        def wrapper(user, *args, **kwargs):
            if user.get('role') != role:
                raise PermissionError(f'Доступ запрещен для роли {user.get('role')}')
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@required_access('admin')
def delete_user(user, username):
    print(f'Пользователь {username} был удален администратором {user.get('role')}')

user_1 = {"user": 'petr', "role": 'root'}
user_2 = {"user": 'stas', "role": 'admin'}

# delete_user(user_1, 'test_user') вызов исключения
delete_user(user_2, 'test_user')