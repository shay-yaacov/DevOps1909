from unittest import removeResult


def azret(number):
    if number== 0:
        return 1
    else:
        return number * azret(number-1)

def not_recursion (number):
    sum = 1
    while (number > 1):
        sum = sum*number
        number = number-1
    return sum




num = input("enter a number: ")
print (azret(int(num)))

result= not_recursion(int(num))
print (result)