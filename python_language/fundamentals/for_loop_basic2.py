"""
#biggie size
def biggie(list):
    y = []
    for i in list:
        if i > 0:
            i = 'big'
        y.append(i)
    return y
print(biggie([1,-2,3,-3]))

# count positives
def count(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list.append(count)
    return list
print(count([-1,-1,1,1,3]))

# sum total
def sumT(list):
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x
print(sumT([1,2,3,4]))

#Average
def avg(list):
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x / len(list)
print(avg([1,2,3,4]))

#Length
def length(list):
    return len(list)
print(length([1,2,3]))

#minimum
def mini1(list):
    if len(list) == 0:
        return False
    mini = list[0]
    for i in range(0, len(list), 1):
        if list[i] < mini:
            mini = list[i]
    return mini
print(mini1([77,-2,-70,1,-1]))

#maximum
def maxx1(list):
    if len(list) == 0:
        return False
    max1 = list[0]
    for i in range(0, len(list), 1):
        if list[i] > max1:
            max1 = list[i]
    return max1
print(maxx1([77,5552,-70,1,-1]))

#ultimate analysis
def ult(list):
    sumTotal = 0
    average = 0
    minimum = 0
    maximum = 0
    length = 0
    for i in range(0, len(list), 1):
        sumTotal += list[i]
        average = sumTotal / len(list)
        length = len(list)
        if list[i] < minimum:
            minimum = list[i]
        if list[i] > maximum:
            maximum = list[i]
    new_dict= {"sumTotal":sumTotal, "average": average, "minimum": minimum, "length": length, "maximum":maximum}
    return new_dict 
print(ult([37,2,1,-9])) 
"""
# reverse list
def rev(list):
    for i in range(0, len(list)/2, 1):
        temp = list[i]
        list[i] = list[len(list)-1-i]
        list[len(list)-1-i] = temp
    return list
print(rev([1,2,3,4,5,6]))

