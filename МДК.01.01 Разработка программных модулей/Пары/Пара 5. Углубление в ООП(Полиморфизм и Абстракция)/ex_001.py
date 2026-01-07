"""
https://drive.google.com/file/d/1u09rhX85Ydnzy1H5UW5zDCciekCepWpq/view?usp=drive_link - презенташка
"""

class Write:
    def do(self):
        print('Мы что-то написали!')

class Read:
    def do(self):
        print('Мы что-то напечатали!')

def pc_do(obj):
    obj.do()

compucters_do = [Write(), Read()]

for pc in compucters_do:
    pc_do(pc)