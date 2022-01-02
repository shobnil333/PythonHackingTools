import string
from random import *

characters = string.ascii_letters + string.digits + string.punctuation
output = open('passwordlist.txt', 'a')

for x in range(0, 100):
    password = "".join(choice(characters) for i in range(randint(8, 16)))
    output.write('%s\n' % password)
