'''
context - нужен для хранения данных о состоянии авторизированного пользователя
'''

class AppContext:
        _instance = None

        def __new__(cls):
                if cls._instance == None:
                        cls._instance = super().__new__(cls)
                        cls._instance._reset_state()
                return cls._instance
          
        def _reset_state(self):
                self.is_authenticated = False
                self.current_user_id = None
                self.current_username = "guest"

        def login(self,  user_id:  int, username: str):
                self.is_authenticated = True
                self.is_user_id = user_id
                self.current_username = username

        def logout(self):
                self._reset_state()

        def require_auth(self)  -> bool:
                return self.is_authenticated
        
        def get_user_id(self)->int:
                if not self._is_authenticated:
                        raise RuntimeError("Ошибка получения данных id пользователя")
                
app_context = AppContext()