from main import *

def testSum():
    assert getSum(3, 5) == 8

def testLength():
    assert getLength("Са") > 3

def testAge():
    assert getAge(17) > 18

# Ctrl + Shift + P -> Python: Configure Tests