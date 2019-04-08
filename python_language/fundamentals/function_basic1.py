#1
"""
def a():
    return 5
print(a())
#returns 5
#2
def a():
    return 5
print(a()+a())
#returns 10
#3
def a():
    return 5
    return 10
print(a())
#return 5
#4
def a():
    return 5
    print(10)
print(a())
#return 5
#5
def a():
    print(5)
x = a()
print(x)
#prints 5
#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
#prints 8
#prints 3 then 5 then a typError
#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#25
#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 1
    return 7
print(a())
#print 100 return 10
#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
#returns 7, 14, 21
#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
#returns 8
#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
#prints 500 then again 500 then 300 then 500
#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#prints 500 then 300 then return 300  then 500 then 500 return 300 then 500
#prints 500,500,300,500
#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#prints 500, 500, 300, 300
#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
#1,3,2
"""
#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
#prints 1,3,5,10