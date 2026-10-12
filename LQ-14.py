import matplotlib.pyplot as plt
month=[1,2,3,4,5,6,7,8,9,10,11,12]
profit=[10,20,30,40,20,30,14,25,34,10,22,14]
plt.plot(month,profit,color='green',marker=".")
plt.xlabel("month in number",color='red')
plt.ylabel("total profit (in lakh)",color='red')
plt.title("PROFIT MADE BY COMPANY ABC",fontsize=20)
plt.grid(True,linestyle='-.',color='blue')
plt.xticks(month)
plt.yticks(profit)
plt.show()
