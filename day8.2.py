#
# Just another method I Found of doing day 8
#
import sys

entries = int(sys.stdin.readline())
phoneBook = {}

for i in range(entries):
    key, value = sys.stdin.readline().split()
    phoneBook[key] = value

while True:
    key = sys.stdin.readline().strip()
    if key == '':
        break
    elif key in phoneBook:
        print(key + '=' + phoneBook[key])
    else:
        print('Not found')




