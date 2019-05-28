from read_file import*
from sample_ui import*
import math
filename="exponential_data_generation.txt"
n=len(data) #n=number of observations
min1=2222
max1=0
for i in range(0,len(data)-1):
	if(data[i]>max1):
		max1=data[i]
	if(data[i]<min1):
		min1=data[i]
print("min=",min1)
print("max=",max1)
print("Number of observation(n)=",n)
k=int(input("Number of intervals:"))
pj=1/k
print("Pj(probability)=",pj) #probability
Ej=n*pj
print("Expected frequency=",Ej)
#interval=(max1-min1)/k
#print("interval=",interval)
lamb=0.0
sum1=0.0
mean=0.0
for i in range(0,len(data)-1):
	sum1=sum1+data[i]
	mean=sum1/n
	lamb=1/mean
#print("\nsum=",sum1) #Summation Xi
print("lambda=",lamb)
#print("mean=",mean)
ai=[]
list1=[]
ln_list=[]
for i in range(0,k):
	l2=1-(i*pj)
	list1.append(l2)
#print("\nvalue_list=",list1)
for i in range(0,len(list1)):
	ln_list.append(log(list1[i]))	
	l1=(-1)/(lamb)
	l3=l1*ln_list[i]
	ai.append(l3)
#print("\nai=",ai)   
#find oj_list:
oj_list=[]
for i in range(0,len(ai)-1):
	cnt=0
	for j in range(0,len(data)-1):
		if (data[j]>=ai[i] and data[j]<ai[i+1]):
			cnt+=1	
	oj_list.append(cnt)	
	i=i+1
#print("\noj_list",oj_list)
chi_sq=0.0
chi_sq_list=[]
sum2=0.0
for i in range(0,len(oj_list)):
	sum2=((oj_list[i]-Ej)**2)/Ej
	chi_sq_list.append(sum2)
for i in range(0,len(chi_sq_list)):
	chi_sq+=chi_sq_list[i]	
print("Chi_square=",chi_sq)
#########Comfirmation Parameters:##########
cv=0.0
var_x=0.0
l=0.0
for i in range(0,len(data)-1):
	l+=(data[i])**2
var_x=(l-n*mean)/(n-1)
print("Var(x)=",var_x)
d=(abs(var_x)/mean)
cv=math.sqrt(d)
print("CV=",cv)
#____________________data_generation_____________________-##
xi=[]
ln_ui=[]
for i in range(0,len(ui)):
        lk=log(1-(ui[i]))
        ln_ui.append(lk)
#print("ui_log(x)=",ln_ui)
for g in range(0,len(ln_ui)):
        x=-mean*(ln_ui[g])
        xi.append(x)
#print("xi_values=",xi)
with open(filename,'w')as f:
        for item in xi:
                f.write("%s\n"% item)
