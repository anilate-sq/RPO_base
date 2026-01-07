class Airplane:
      def fly(self):
            print('Полетели')

class Ship:
      def fly(self):
            print('Корабль полетел, что??')
      def swim(self):
            print('Поплыли')

class Car(Ship, Airplane):

      def drive(self):
         print('Вин Дизель')

c = Car()
c.fly()
c.drive()
c.swim()
