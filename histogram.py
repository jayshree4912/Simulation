import numpy as np
import matplotlib.pyplot as plt
import sys

filename=sys.argv[1]

file1=open(filename,"r")

data=[]

for i in file1.readlines():
	data.append(float(i))

lower=min(data)
upper=max(data)

freq=[]
Range=[]
size=(upper-lower)/10
count=0
i=0
while i<10:
    for j in data:
        if(j>=lower and j<lower+size):
            count+=1
    freq.append(count)
    Range.append(str(lower) + "-" + str(lower+size))
    count=0
    lower+=size
    i+=1

plt.bar(Range,freq,align='center')
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.gcf().autofmt_xdate()
plt.show()
