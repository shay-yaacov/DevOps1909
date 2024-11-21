
current_name = input ("what is your name? ")
while current_name != "quit":
    current_name = input("what is your name? ")
    if current_name == "eden":
        continue
    if current_name == "ronen":
        break
    print (f" Hello  {current_name}")
    current_name = input ("what is your name? ")
else:
    print ("goodbye")

i = 40
for i in range(5):
    print (i)

print  ("------")
print (i)



