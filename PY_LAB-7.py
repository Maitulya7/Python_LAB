# 1) Write a python program to average all numbers from the given list

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    elem=int(input("Enter element: "))
    a.append(elem)
avg=sum(a)/n
print("Average of elements in the list",round(avg,2))


# 2) Write a python program to delete a specific element (all occurrence)  from the user list.

print(end="Enter the Size of List: ")
tot = int(input())

arr = []
print(end="Enter " +str(tot)+ " Elements: ")
for i in range(tot):
    arr.append(input())

print(end="\nEnter the Value to Delete: ")
val = input()

if val in arr:
    arr.remove(val)
    print("\nThe New list is: ")
    for i in range(tot-1):
        print(end=arr[i]+" ")
else:
    print("\nElement doesn't exist in the List!")


# 3) Write a python program to delete all duplicate elements from a list


def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(Remove(duplicate))


# 4) Write a python program to find intersection and union of two list  elements.

def intersection_list(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3

def Union(lst1, lst2):
	final_list = lst1 + lst2
	return final_list

list1 = [40, 90, 11, 58, 31, 66, 28, 54, 79]
list2 = [58, 90, 54, 31, 45, 11, 66, 28, 26]
print(intersection_list(list1, list2))
print(Union(list1, list2))

# 5) Write a Python program to flatten a nested list or list of lists.
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)

# 6) Write a Python program to find the repeated items of a tuple.

tup=(1,3,4,32,1,1,1,31,32,12,21,2,3)
for i in tup:
    if tup.count(i) > 1:
        print(i)

# 7) Write a Python program to convert a list to a tuple.

listx = [5, 10, 7, 4, 15, 3]
print(listx)
tuplex = tuple(listx)
print(tuplex)

# 8) Write a Python program to convert a tuple to a dictionary

tuplex = ((2, "w"),(3, "r"))
print(dict((y, x) for x, y in tuplex))

# 9) Write a Python program to find the index of an item of a tuple.

numtup = (11, 33, 55, 77, 99, 111, 77, 121, 13, 55, 77)
print(numtup)

index1 = numtup.index(33)
print("Index Position of 33 = ", index1)

index2 = numtup.index(77)
print("Index Position of 77 = ", index2)

index3 = numtup.index(77, 4)
print("Index Position of 77 = ", index3)

index4 = numtup.index(77, 7)
print("Index Position of 77 = ", index4)


# 10) Write a Python program to reverse a tuple.

def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

tuples = ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
print(Reverse(tuples))

