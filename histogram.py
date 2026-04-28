import pandas as pd
import matplotlib.pyplot as plt


plt.style.use("ggplot")
age=[22,55,30, 25, 40, 45, 45, 50]

# bin: amount of group that data set will be divided into 5, so in range 22-50 will divided into 5 groups
# or initilise bins with our own range
bin=[10, 20, 30, 40, 50] # group 1 from 10-20, group 2 from 20-30, group 3 from 30-40, ..
plt.hist(age, bins=bin, edgecolor="black")

median_age=33
plt.axvline( median_age, color="k", label="Median_age")
# ax vetical line: to show median age

plt.title("Age distribution")
plt.xlabel("Age_ groups")
plt.ylabel("Number of people")
plt.show()


