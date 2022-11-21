# 1) Write a python program that takes meter as input and converts it  into feet and inches.

input1 = input('feet to meter or meter to feet? ')

if input1 == 'feet to meter':
    feet = float(input('enter feet: '))
    meter = feet *0.3048
    print(meter)

if input1 == 'meter to feet':
    meter = float(input('enter meter: '))
    feet = meter/0.3048
    print(feet)


# 2) Write a python function that finds the decimal equivalent of the binary number 10011?

binary = input("Enter a binary number:")

def BinaryToDecimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)

BinaryToDecimal(binary)

# 3) Write a python function that finds the equivalent Hexa-decimal code and octal code for the decimal number 191.

dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")



# 4) Write a python function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise.

x=input('Enter string #1: ')
y=input('Enter string #2: ')

def isIn(x,y):
    if x in y:
       return True
    elif y in x:
        return True
    else:
        return 'False'

print(isIn(x,y))