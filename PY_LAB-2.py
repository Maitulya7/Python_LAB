print("\n")
print("===============================================================")
print("1.Python program to check if the input number is odd or even.")


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   
   
print("\n")
print("===============================================================")
print("2.write a program to check if given number is positive or negative or zero")


n = float(input('Input a number: '))
print('Number is Positive.' if n > 0 else 'It is Zero!' if n == 0 else 'Number is Negative.')
   


print("\n")
print("===============================================================")
print("3.write a program to swap the two number without using temporary variables")


x = 5
y = 7

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# code to swap 'x' and 'y'
x, y = y, x

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
   

print("\n")
print("===============================================================")
print("4.write a program to find largest amoung given three numbers")

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

largest = 0

if a > b and a > c :
    largest = a
elif b > c :
    largest = b
else :
    largest = c

print(largest, "is the largest of three numbers.") 



print("\n")
print("===============================================================")
print("5.write a program to sum of odd and even number from 1 to 10")  


max=int(input("please enter the maximum value: "))
even_Sum=0
odd_Sum=0

for num in range(1,max+1):
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num

print("The sum of Even numbers 1 to {0} = {1}".format(num,even_Sum))
print("The sum of odd numbers 1 to {0} = {1}".format(num,odd_Sum))


print("\n")
print("===============================================================")
print("6.write a program make a simple calculator that can add , subtract , multiply and divide using user choice")  


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")


print("\n")
print("===============================================================")
print("7.write a program to calculate spi using given marks")  