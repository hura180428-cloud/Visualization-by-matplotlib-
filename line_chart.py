from matplotlib import pyplot as plt
# print (plt.style.available) chi tim so luonng style co the bieu dien vowi cacs bieu do nay
# after choosing style. plt.sue ("# ten style muon dung")
dev_x=[25, 27, 30, 33, 35]
dev_y=[1000, 1200, 2000, 2500, 4000]
# mau, dang net, markers, ...
# color co the dung he thap luc color="#4444", thickline =linewidth, 
plt.plot( dev_x, dev_y, color="k", linestyle="--", marker=".", linewidth=3)# # truc x, truc y, co the them label chi them argurment: label="")
# plt.plot ( dev_x, median_y) # vi du bieu do thu 2
plt.title(" Median salary versus age")
plt.xlabel(" Age")
plt.ylabel("Median_salary (usd)")
plt.legend("Salary") # co the cos hai bien, sx theo thu tu truyen vao cua thong so y, co the ve chung 1 bieu do, chung truc x, trucj y khac nhau
plt.savefig("Name.png")# digsignate specific type of image
plt.show() # show values


