import requests
with open("names.txt","r") as my_file: # there is no need to close the file

    names = my_file.read().splitlines()
    for name in names:
         print(name)

print (my_file)
with requests.get ("https://api.github.com/users/avielb/repos") as response:
    response.raise_for_status()
