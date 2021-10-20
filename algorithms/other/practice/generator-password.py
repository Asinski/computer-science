import string
import random
import os


letters, numbers, symbols = string.ascii_letters, string.digits, string.punctuation
all = letters + numbers + symbols

length = int(input())

password = ''.join(random.sample(all, length))

os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))
with open("password.txt", "w") as pw:
    pw.write(password)
