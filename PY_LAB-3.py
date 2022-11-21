 # 1. Write a Python program to find out the sum of all digits of a number

n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)

# 2) Write a Python program to print all combinations o f three numbers.

 # Python program to print all
 # the possible combinations

 def comb(L):
     for i in range(3):
         for j in range(3):
             for k in range(3):

                 # check if the indexes are not
                 # same
                 if (i != j and j != k and i != k):
                     print(L[i], L[j], L[k])


 # Driver Code
 comb([1, 2, 3])

# 3) Write a Python program to calculate total vowels in a string .

string=raw_input("Enter string:")
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)

# 4) Python program to find the smallest and largest divisor o f a number.

num = int(input("Enter a number : "))
for i in range(2, num+1):
    if num % i == 0:
        print ("The smallest divisor for {} is {}".format(num, i))
        break

largest_divisor = 0
for i in range(2, num):
    if num % i == 0:
        largest_divisor = i

    print("Largest divisor of {} is {}".format(num,largest_divisor))

# 5) Write a python program to reverse a number.

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

# 6) Write a python program to check if a number is abundant/excessive or not.

input_no = int(input("Enter a number : "))
total = 0
is_abundant = 0

for i in range(1,input_no):
  if(input_no % i == 0):
    total = total + i
    if(total > input_no):
      is_abundant = 1
      break
if((total > input_no) or (is_abundant ==1)):
  print("It is an abundant number.")
else :
  print("It is not an abundant number.")



# 7) Write a python program to check if a year is a leap year or not.

year = 2000

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

# 8) Write a python program to display all the prime numbers within an  interval range given by user.


lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")
for number in range(lower_value, upper_value + 1):
     if number > 1:
         for i in range(2, number):
             if (number % i) == 0:
                 break
         else:
             print(number)

# 9) Write a python program to check if a string is palindrome or not.

def isPalindrome(s):
	return s == s[::-1]

s = "malayalam"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

# 10) Write a program to print the following pattern in output console  window.

# 1

 # 1
 # 12
 # 123
rows = 5
for row in range(1, rows+1):
    for column in range(1, row + 1):
        print(column, end="")

    print()

# 2

 # 1
 # 22
 # 333
rows = 6

for num in range(rows):

    for i in range(num):

        print(num, end="")

    print()

# 3 Equilateral Triangle with Stars
print('Print equilateral triangle Pyramid using stars')

size = 7

m = (2 * size)-2

for i in range(0, size):

    for j in range(0, m):

        print(end="")

    m = m-1 # decrementing m after each loop

    for j in range(0, i + 1):

        # printing full Triangle pyramid using stars

        print("*", end="")

    print("")

# 4 Downward Triangle Pattern of Stars

rows = 5

k = 2 * rows-2

for i in range(rows, -1, -1):

    for j in range(k, 0, -1):

        print(end="")

    k = k + 1

    for j in range(0, i + 1):

        print("*", end="")

    print()

# 5 Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern")
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
