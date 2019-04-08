"""
#countdown
def countdown(arr):
    y = []
    for x in range(arr, -1, -1):
        y.append(x)
    return y
print(countdown(5))

#print and return
def pandr(list):
    print(list[0])
    return list[1]
z = pandr(1,5)
print(z)

#first plus length
def list(myList):
    x = myList[0]
    y = len(myList)
    print(x + y)
     
list([1,2,3])
# values greater than second
def list(myList):
    newList = []
    for i in myList:
        print(i)
        print('-------')
        if len(myList) < 2:
            return False
        elif i > myList[1]:
            newList.append(i)
    return newList
print(list([1,2,3]))
"""
#this length that value
def lenVal(size, value):
    y = []
    for i in range(0, size, 1):
        y.append(value)
    return y
a = lenVal(4,7)
print(a)