import string
from random import *

characters = string.ascii_letters + string.digits + string.punctuation
input_num = int(input('Enter number of password you want to generate: '))
output = open(input('Enter file name you want to save passwords: '), 'a')

for num in range(input_num):
    password = "".join(choice(characters) for i in range(randint(16, 20)))
    output.write('%s\n' % password)
