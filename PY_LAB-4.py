# 1)Write a Python program to find the LCM o f two numbers.

def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

# 2)Write a Python program to find if a number is Armstrong or not.

num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# 3)Write a Python program to find the total number o f lowercase  characters in a string.

string=raw_input("Enter string:")
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

# 4)Write a program to remove characters from odd or even index of a  string.

input_string = input("Enter a string : ")

output_string = ""

oddOrEven = int(input("Enter '1' if you want to remove odd positioned characters , '2' for even positioned characters : "))

if oddOrEven ==1 :
  print ("String after removing characters on odd position : ")
  for i in range(len(input_string)):
    if i%2 != 0:
      output_string = output_string + input_string[i]

elif oddOrEven == 2 :
  print ("String after removing characters on even position : ")
  for i in range(len(input_string)):
    if i%2 == 0:
      output_string = output_string + input_string[i]

print (output_string)


# 5)Write a python program to merge two lists and sort it.

a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)

# 6)Write a python program to print one identity matrix

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",sep=" ",end=" ")
        else:
            print("0",sep=" ",end=" ")
    print()