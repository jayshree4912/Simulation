from read_file import*
from sample_ui import*
mean=0.0
var_x=0.0
s=0.0
filename="uniform_data_generation.txt"
for i in range(0,len(data)):
	s+=data[i]
#print("Sum=",s)
n=len(data)
#print("N=",n)
mean=s/n
print("Mean=",mean)
l=0.0
for i in range(0,len(data)):
	l+=(data[i])**2
#print("l=",l)
var_x=(l-n*(mean)**2)/(n-1)
print("Var(x)=",var_x)
a=0.0
b=0.0
h=2*mean
j=math.sqrt(12*var_x)
#print("a+b",h)
#print("b-a",j)
a=(h-j)/2
print("a=",a)
b=h-a
print("b=",b)
k=int(input("Enter Value of K:"))
pj=1/k
#print("pj=",pj)
Ej=n*pj
#print("Ej=",Ej)
ai=[]
for i in range(0,k):
	l=(i*pj*(b-a))+a
	ai.append(l)
#print("ai=",ai)
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
###_________data generation__________##
xi=[]
for i in range(0,len(ui)):
        x=((b-a)*ui[i])+a
        xi.append(x)
#print("Xi_random data=",xi)

with open(filename,'w')as f:
        for item in xi:
                 f.write("%s\n" % item)
                 
