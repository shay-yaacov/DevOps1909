
current_name= input ("what is your name? ")

my_file = open ("names.txt", 'a')
my_file.write (current_name + "\n")
my_file.close()

mt_file = open ("names.txt", 'r')
for name in mt_file.readlines():
    print (name)
    print (f"hello {name.strip()}")
my_file.close()

