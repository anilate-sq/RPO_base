"""
Контекст приложения: хранение состояния авторизованного пользователя
"""

class AppContext:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._reset_state()
        return cls._instance

    def _reset_state(self):
        self.is_authenticated = False
        self.current_user_id = None
        self.current_username = "guest"

    def login(self, user_id: int, username: str):
        self.is_authenticated = True
        self.current_user_id = user_id  
        self.current_username = username

    def logout(self):
        self._reset_state()

    def require_auth(self) -> bool:
        return self.is_authenticated

    def get_user_id(self) -> int:
        if not self.is_authenticated:  
            raise RuntimeError("Попытка получения ID пользователя без авторизации")
        return self.current_user_id  

app_context = AppContext()