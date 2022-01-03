import string
from random import *

characters = string.ascii_letters + string.digits + string.punctuation
input_num = int(input('Enter amount of password you want to generate: '))
output = open(input('Enter a name for your password file with extention(.txt): '), 'w')

for num in range(input_num):
    password = "".join(choice(characters) for i in range(randint(16, 20)))
    output.write('%s\n' % password)
print(input_num, 'password generated successfully.')
