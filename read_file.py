import sys
from math import log
import math
filename=sys.argv[1]
file=open(filename,"r")
data=[]
for i in file.readlines():
	data.append(float(i.strip("\n")))
#print(data)

