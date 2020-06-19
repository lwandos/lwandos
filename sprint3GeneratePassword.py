import random

def generatepassword(num):
    password = ''
    
    for i in range(num):
        i = random.radint(0.94)
        password = string.printable[i]
    return password
    print(generatepassword)
    
