class A:
       def hello(self):
           print('A')

class B(A):
       def hello(self):
           super().hello()
           print('B')
class C(A):
      def hello(self):
            super().hello()
            print('C')

class D(B, C):
     def hello(self):
           super().hello()
           print('D')   

d = D()
d.hello()

