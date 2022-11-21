# 1) Write a python program to create a new file

f = open("myfile.txt", "x")

# 2) Write a python program to read a file.

f = open("myfile.txt", "r")

# 3) Write a Python program to append text to a file and display the text.

f=open("myfile.txt", "a+")

for i in range(5):

     f.write("Appended line %d\r\n" % (i+1))


# 4) Write a Python program to read a random line from a file.

import random

print(random.choice(open("myFile.txt","r").readline().split()))


# 5) Write a python program to count the number of words in a file

file = open("C:\data.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))

# 6) Write a python program to count the number of blank spaces in a file.

file = open("test1.txt", "r")

count = 0
while True:

    char = file.read(1)

    if char.isspace():
        count += 1
    if not char:
        break

print(count)

# 7) Write a python program to count the total number of lines in a file.

with open(r"myfile.txt", 'r') as fp:
	lines = len(fp.readlines())
	print('Total Number of lines:', lines)


# 8) Write a python program to find the longest words.

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))

# 9) Write a Python program to count the frequency of words in a file.

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))

# 10) Write a Python program to copy the contents of a file to another file.

with open('first.txt', 'r') as firstfile, open('second.txt', 'a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
