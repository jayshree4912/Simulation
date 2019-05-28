import matplotlib.pyplot as plt
import sys 
filename=sys.argv[1]
file=open(filename,"r")
data=[]
for i in file.readlines():
	data.append(float(i.strip("\n")))
#print(data)
y=data[1:]
y.append(data[0])
plt.scatter(data,y,marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
