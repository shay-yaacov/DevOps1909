print ("hellow")
a = 5
b = 3

c = a + b
print (c)

myDict = {"name": "aviel",
 "age": 28,
 "hobbies": ["Skiing", "Cooking"],
 "children": None}
print(myDict["name"])
myDict["age"] = 29
print(list(myDict.keys()))
print(list(myDict.values()))
print("Enter your name:", end =" ")
#name = input()
#print("Have a good day " + name)

def dict_validator(dict_to_validate):
    if dict_to_validate.get('name') is None or not type(dict_to_validate.get('name')) is str:
       print("missing or incorrect type field: name")
       print (dict_to_validate)
       print("first if")
    if dict_to_validate.get('age') is None or not type(dict_to_validate.get('age')) is int:
       print("missing or incorrect type field: age")
       print(dict_to_validate)
       print("second  if")
    if dict_to_validate.get('hobbies') is None or not type(dict_to_validate.get('hobbies')) is list:
       print("missing or incorrect type field: hobbies")
       print(dict_to_validate)
       print("thirda"
             " if")


dict_validator({"name": "aviel"})
print("--------------")
dict_validator({"name": 234})
print("--------------")
dict_validator({"name": "aviel", "age": 28})
print("--------------")
dict_validator({"name": "aviel", "age": 28, "hobbies":["teaching", "DevOps", "playing the uke"]})

for x in range(5):
    print(x)