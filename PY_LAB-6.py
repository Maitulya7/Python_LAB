# 1) Create a Python function to take user input and check validity of a  password.

import re
p= input("Input your password")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")

# 2) Create a python function that sort all words o f a user String in Alphabetical order.

my_str = input("Enter a string: ")
words = my_str.split()
words.sort()
for word in words:
   print(word)

# 3)Create a Python function that check if a enter date is valid or not.

import datetime
correctDate = None
try:
    newDate = datetime.datetime(2008,11,42)
    correctDate = True
except ValueError:
    correctDate = False
print(str(correctDate))

# 4)Create a Python function that find the number of days between two dates.


from datetime import date

def numOfDays(date1, date2):
    return (date2 - date1).days

date1 = date(2018, 12, 13)
date2 = date(2019, 2, 25)
print(numOfDays(date1, date2), "days")
