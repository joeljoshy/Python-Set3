
import re

string = '''Number 1: 0123456789'''


phone=re.compile(r'\d{10}')
match = phone.findall(string)


if match:
    print('Mobile number found from the string : ')
    for i in match:
      print(i)
else:
    print("No numbers found!!")
