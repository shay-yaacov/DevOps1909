
name: str ="a"
age: int = 20

def greet(name: str) -> str:
    return f"Hello {name}!"

print (greet ("shay"))



def check_in_interval (what_to_ask,min, max,what_to_print):
    current_value = int(input(what_to_ask))
    if min < current_value < max:
        print (what_to_print)

def square(n):
    print (n*n)

square (5)


check_in_interval("Enter your age ", 0, 20, "Your are ok")
check_in_interval("Enter your year of experience ", 2, 5, "You are experienced")

