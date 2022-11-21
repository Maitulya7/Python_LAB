# 1) Write a python program to create a line plot on the basis of selected  database.

import matplotlib.pyplot as plt

year = [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
unemployment_rate = [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]

plt.plot(year, unemployment_rate)
plt.title('unemployment rate vs year')
plt.xlabel('year')
plt.ylabel('unemployment rate')
plt.show()

# 2) Write a python program to create a pie plot on the basis of selected  database.


from matplotlib import pyplot as plt
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]
fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=cars)
plt.show()


# 3) Write a python program to create a bar and barh plot on the basis of  selected database.

import numpy as np
import matplotlib.pyplot as plt

data = {'C':20, 'C++':15, 'Java':30,'Python':35}
courses = list(data.keys())
values = list(data.values())
fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon',width = 0.4)
# creating the barh plot
plt.barh(courses, values, color='maroon')

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()

# 4) Write a python program to create a histogram plot on the basis of  selected database

from matplotlib import pyplot as plt
import numpy as np
a = np.array([22, 87, 5, 43, 56,73, 55, 54, 11,20, 51, 5, 79, 31,27])
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(a, bins = [0, 25, 50, 75, 100])
plt.show()

# 5) Write a python program to create a scatter plot on the basis of selected  database

import matplotlib.pyplot as plt

price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales_per_day = [34, 62, 49, 22, 13, 19]

plt.scatter(price, sales_per_day)
plt.show()

# 6) Write a python program to create a subplot contain four different lineplot from the database.

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()