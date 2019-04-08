"""
#update values in dictionaries and list
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name': 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y']= 30
print(z)

#iterate through a list of dictioanries

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(students):
    for i in students:
        print('first_name - '+ i['first_name']+ ', ' + 'last_name - ' + i['last_name'] )


iterateDictionary(students)

#get values from a list of dictionaries
def iterateDictionary2(key_name, some_list):
    for i in students:
        if key_name == 'first_name':
            print(i['first_name'])
        elif key_name == 'last_name':
            print(i['last_name'])

iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)
"""

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(myDict):
    for key in myDict:
        print(len(myDict[key]), key )
        arr = myDict[key]
        for k in arr:
            print(k)

printInfo(dojo)
