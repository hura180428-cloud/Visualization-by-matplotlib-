# bar_chart with multi bar in one graph
from matplotlib import pyplot as plt
import numpy as np
# print (plt.style.available) chi tim so luonng style co the bieu dien vowi cacs bieu do nay
# after choosing style. plt.sue ("# ten style muon dung")
dev_x=[25, 27, 30, 33, 35]
dev_y1=[1000, 1200, 2000, 2500, 4000]
dev_y2=[1500, 1800, 2500, 3000, 5000]
x_indexes=np.arange (len(dev_x)) 
#  create x axis to shift bar a distance equal width
width=0.30
# mau, dang net, markers, ...
# color co the dung he thap luc color="#4444", thickline =linewidth, 
plt.bar(x_indexes-width, dev_y1, color="g", width=0.25, label="Group 1")# # truc x, truc y, co the them label chi them argurment: label="")
# plt.plot ( dev_x, median_y) # vi du bieu do thu 2
plt.bar( x_indexes, dev_y2, color="b", width=0.25, label="Group2")
plt.title(" Median salary versus age")
plt.xlabel(" Age")
plt.ylabel("Median_salary (usd)")
plt.xticks(ticks=x_indexes, labels=dev_x) # recreate x_axis
# plt.legend("Salary") # co the cos hai bien, sx theo thu tu truyen vao cua thong so y, co the ve chung 1 bieu do, chung truc x, trucj y khac nhau
plt.savefig("Name.png")# digsignate specific type of image
plt.show() # show values

# if the graph is too crowded, we can change vertical bar into horozontal bar with plt.barh


