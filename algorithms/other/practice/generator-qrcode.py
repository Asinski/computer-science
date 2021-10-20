import pyqrcode
import os
from random import sample
from string import ascii_letters

qrstring = input(r'')
url = pyqrcode.create(qrstring)
os.chdir(os.path.join(os.path.expanduser('~'), 'Desktop'))
url.png(f'{"".join(sample(ascii_letters, 4))}.png', scale=9)
