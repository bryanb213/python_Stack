# another way to iterate through the keys
capitals = { "name": "Noelle", "language": "Python" }
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)

