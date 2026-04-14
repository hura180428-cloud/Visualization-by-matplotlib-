import matplotlib.pyplot as plt

plt.style.use( "fivethirtyeight") # stype of the graph, you can check available styles with plt.style.available
# slices=[60, 40, 30, 20] # the proportion will be forced into 100%
# color=["yellow", "red", "blue", "green"] # choose color for each slice, used hex color code or color name
slices = [59219, 55466, 47544, 36443, 35917]
label = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explodes=[0, 0, 0, 0, 0.1] # to emphasize a slice than the others.


plt.pie(slices, labels=label,wedgeprops={'edgecolor':'black'}, explode=explodes, shadow=True, 
        startangle=90, autopct='%1.1f%%')
# meaning of the parametters: data, labels, adgecolor, explode to emphasize a slice, shadow but i think it should not present
#startangle to designate the starting point, can the last is to show data
plt.title ("My money")
plt.tight_layout()
plt.show()