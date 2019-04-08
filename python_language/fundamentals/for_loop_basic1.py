"""#Basic
for i in range(0, 151, 1):
    print(i)

#multiples of 5
for k in range(5,1000,5):
    print(k)

#counting, the dojo way

for x in range(1,101):
    if x % 10 == 0:
        print("Dojo")
    
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

#whoa, that suckers huge
for x in range(0,500000,2):
    sum = 0
    sum += x
print(sum)

#countdown by fours
for x in range(2018, 0, -4):
    print(x)
"""
# flexible counter
lowNum = 2
highNum = 10
mult = 3
for x in range(lowNum, highNum, 1):
    if x % mult == 0:
        print(x)