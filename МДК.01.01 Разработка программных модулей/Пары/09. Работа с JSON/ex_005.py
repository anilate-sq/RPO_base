import json

class User:
      def __init__(self, name, age):
            self.name = name
            self.age = age
      def encode_user(obj):
            return obj.__dict__
      
      def decode_user(dct):
            if "name" in dct and "age" in dct:
                  return User(dct["name"], dct["age"])
            return dct
#     raise TypeError("Объект не подлежит сериализации")
data_json_str = '{"name": "Виталик", "age": 15}'
json.loads(data_json_str, object_hook=User.decode_user)

data = json.dumps(User("Alex", 30), default=User.encode_user)
print(data)