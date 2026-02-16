'''
Data Access Layer(DAL) - Слои управления данными

Основные виды:
    - Data Access Object(DAO)
    - Repository

Примерная структура:

DAO:
- db
    |_conn.py
- services
    |_table_name1Service.py
    |_table_name2Service.py
- ui
    |_mainWindow.py
    |_authWindow.py
    |_regWindow.py
    |_profileWindow.py
- main.py         

Repository: 
- db
    |_conn.py
    |_data1Repository.py
    |_data2Repository.py
- ui
    |_mainWindow.py
    |_authWindow.py
    |_regWindow.py
    |_profileWindow.py
- main.py         

'''

