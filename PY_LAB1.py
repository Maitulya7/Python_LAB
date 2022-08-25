print("\n")
print("================================================================")
print("Arithmetic Operator:")
print("================================================================")
# 1
print("1.The mul of 10 and 5 is :", 10*5)

#2
print("2.The sum of 20 and 66 is:", 20+66)

#3
print("3.The sub of 88 and 52 is:", 88-52)

#4
print("4.The div of 20 and 6 is:", 20/6)

#5
print("5.The mod of 52 and 4 is:", 52 % 4)

#6
print("6.The exp 5 with 66 is:", 5**66)

#7
print("7.The floor div of 20 and 6 is:", 20//6)

print("\n")
# What will be the output of following expression in python

#1
print("1.", 4+5.2-0.2)

#2
print("2.", 9.8-2.1*3),

#3
print("3.", 2*3-4//2),

#4
print("4.", (10+4*2)/9+1)

#5
print("5.", (True or False) and (not(True and False)))

#6
print("6.", (2**3) % 2 == 4)

#7
print("7.", ((2*5)+4)-8 % 3**2)

#8
print("8.", 2.5/0.5/2)

#9
print("9.", 2.5/0.5//2)

#10
print("10.", 5**3+3**4 >= 200)


print("\n")
print("================================================================")
print("Comparison operator:")
print("================================================================")

#1

print("1.55 is grater than 33:", 55 > 33)
print("2.55 is less than 33:", 55 < 33)
print("3.55 is equal to 33:", 55 == 33)
print("4.55 is not equal to:", 55 != 33)
print("5.55 is grater than or equal to 33:", 55 >= 33)
print("6.55 is less than or equal to 33:", 55 <=33)


print("\n")
print("================================================================")
print("Logical operator:")
print("================================================================")

#1

A = True
B = False

print("1.True and False is:", A and B)
print("2.True or False is:", A or B)
print("3.True not is:", not A)
print("4.False not is:", not B)


print("\n")
print("================================================================")
print("Assignment operator:")
print("================================================================")

a = 66
b = 8

#1
a += 3
b += 3
print("1. 66 + 3 is:", a, "and 8 + 3 is:", b)

#2
a -= 3
b -= 3
print("2. 66 - 3 is:", a, "and 8 - 3 is:", b)

#3
a *= 3
b *= 3
print("3. 66 * 3 is:", a, "and 8 * 3 is:", b)

#4
a = 66
b = 8
a /= 3
b /= 3
print("4. 66 / 3 is:", a, "and 8 / 3 is:", b)

#5
a = 66
b = 8
a %= 3
b %= 3
print("5. 66 % 3 is:", a, "and 8 % 3 is:", b)

#6
a = 66
b = 8
a //= 3
b //= 3
print("6. 66 // 3 is:", a, "and 8 // 3 is:", b)

#7
a = 66
b = 8
a += 3
b += 3
print("7. 66 + 3 is:", a, "and 8 + 3 is:", b)


print("\n")
print("================================================================")
print("Membership operator:")
print("================================================================")

var1 = "hello world"
print("1.There is hello in hello world:", "hello" in var1)
print("2.There is no hello in hello world:", "hello" not in var1)

print("3.There is name in hello world:", "name" in var1)
print("4.There is no name in hello world:", "name" not in var1)

b1 = [1, 2, 3, 4, 5]
print("5.5 number is not in b1:", "5" in b1)