# This one does not work on the frikin test case 1 (i'm pissed)

import sys
import re

phoneBook = {}

entries = int(sys.stdin.readline())

for __ in range(entries):
    name = sys.stdin.readline().strip()
    word = re.findall(r'^\w+', name)
    number = re.findall(r'\d+$', name)
    phoneBook[word[0]] = number[0]

print(phoneBook)
for __ in range(entries):
    name = str(sys.stdin.readline().strip())
    valuator = phoneBook.get(name)

    if valuator is None:
        print('Not Found')
    else:
        print(name + '=' + phoneBook[name])




