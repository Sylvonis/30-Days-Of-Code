# This one does not work on the frikin test case 1 (I'm pissed)
#
# I feel Dumb (This works now)

import sys
import re

entries = int(sys.stdin.readline())
phoneBook = {}

for i in range(entries):
    name = sys.stdin.readline().strip()
    word = re.findall(r'^\w+', name)
    number = re.findall(r'\d+$', name)
    phoneBook[word[0]] = number[0]

while True:
    key = sys.stdin.readline().strip()
    if key == '':
        break
    elif key in phoneBook:
        print(key + '=' + phoneBook[key])
    else:
        print('Not found')

