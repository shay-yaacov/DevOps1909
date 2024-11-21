
a = "avaiel"

b= a *5
print (b)
print (list(range(5)))
print (list(range(1,50,10)))
print (list(range(50,10,-3)))
for i in range(5):
    print(i)
    print (a)

names = ["vladi","diana","otir"]
for name in names:
    print (name)
    print (name[::-1])
    print (f"hello {name}")

for i in range(len(names)):
    if names[i] == "otir":
        names[i] = "roey"
    print (f"hello {names[i]}")
print (names)



