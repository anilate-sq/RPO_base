import json
data_json_str = '{"name": "Виталик", "age" 15}'

try:
    data = json.loads(data_json_str) # Преобразовываем JSON в строку
except json.JSONDecodeError as e:
    print('Ошибка преобразования: ', e)


