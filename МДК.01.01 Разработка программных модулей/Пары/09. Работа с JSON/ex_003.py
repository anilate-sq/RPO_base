import json

data = {
       "users": ['Витек', 'Ванек']
}

row = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)

print(row)