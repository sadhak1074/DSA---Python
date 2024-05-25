#creating Dictionary

dictionary = {"name": "Sadhak", "Age": "20", "Profile": "Software Engineer"}
print(dictionary)

#accesing element using key 
print(dictionary['name'])

#accessing using get
print(dictionary.get('Age'))

# creation using Dictionary comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)