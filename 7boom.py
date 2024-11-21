
# number = input ("enter a number")
#
# while int (number % 7 == 0 or ("7" in number)):
#     print ("the number is divisible by 7 or contains the digit 7")
#     number = input("enter a number")
#
# else:
#     print ("goodbuy")

for i in range(1, 101):
    if i % 7 !=0 and ("7" not in str(i)):
        print (i)
result = [i for i in range(1, 101) if i % 7 != 0 and "7" not in str(i)]
print(result)


names = ["natan", "shay","ronec", "aaron"]
result = [name.upper() for name in names if "n" in name]
print (type(result))
print (result)
result = [f"hello:{name} "for name in names if "n" in name]
print (result)




