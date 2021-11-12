"""
https://www.python-lernen.de/funktionen-in-python.htm
https://www.python-lernen.de/rueckgabewert-funktionen.htm
https://www.delftstack.com/de/howto/python/return-multiple-values-python/
"""
def addmult(a,b):
    c=a+b
    d=a*b
    return (c,d)

def addmull(a,b):
    c=a+b
    d=a*b
    return [c,d]

def addmule(a,b):
    c=a+b
    d=a*b
    return c,d

def saghallo():
    print('Hallo, hier spricht meinmodul.')

version = '0.1'

# Ende von meinmodul.py
