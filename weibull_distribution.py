from sample_ui import*
import sys
import math as m
from math import log
s_sq=0.0
s=0.0
alpha0=0.0
g_alpha0=0.0
g_dash_alpha0=0.0
alpha1=0.0
itr=1
filename=sys.argv[1]
var=open(filename ,"r")
a=[]
filename="weibull_generated_data.txt"
xi=[]
for i in var.readlines():
	a.append(float(i.strip(" \n")))
#print(a)
add=sum(a)
#print"sum=",add
n=len(a)
mean=add/n           	#x_bar(mean)
lst=[]
for i in range(0,len(a)-1):
	l=a[i]*a[i]
	lst.append(l)
#print("xi_sq=",sum(lst))
s_sq=((sum(lst))-n*(mean)**2)/(n-1)
#print"s_sq:-",s_sq
s=m.sqrt(s_sq)
#print("S=",s)				#varience(s)
alpha0=mean/s
def fun(alpha0,itr):
	print("Iteration:",itr)
	#print("xi_sq=",sum(lst))
	#print("S=",s)
	#print("alpha0=",alpha0)
	j=n/alpha0
	ln_list=[]
	for i in range(0,len(a)-1):
		l=log(a[i])
		ln_list.append(l)
	ln_sum=sum(ln_list)
	#print("ln_list=",ln_sum)
	xi_ralpha=[]
	for i in range(0,len(a)-1):
			l=((a[i])**alpha0)*(log(a[i]))
			xi_ralpha.append(l)
	val=sum(xi_ralpha)
	#print("value=",val)
	nr=n*val
	xi_a=[]
	for i in range(0,len(a)-1):
		l=a[i]**alpha0
		xi_a.append(l)
	dr=sum(xi_a)
	sec=nr/dr
	#print("Sec=",sec)
	g_alpha0=j+ln_sum-sec
	#print("g_alpha0=",g_alpha0)
	l=(alpha0)**2
	k1=(-n)/l
	#print("k=",k)
	l1=[]
	for i in range(0,len(a)-1):
			l=((a[i])**alpha0)*((log(a[i]))**2)
			l1.append(l)
	val1=sum(l1)
	#print("value=",val1)
	nr1=n*val1
	#print("nr=",nr1)
	b=nr1/dr
	#print("b=",b)
	dr_new=dr**2
	z=nr1/dr_new
	g_dash_alpha0=k1-b+z
	#print("g_dash_alpha0=",g_dash_alpha0)
	alpha1=alpha0-(g_alpha0/g_dash_alpha0)
	#print("alpha1=",alpha1)
	d=alpha1-alpha0
	k2=abs(d)
	#print(k)
	if k2<=0.001:
		print("alpha1",alpha1)
		print("diff=",k2)
		beta=0.0
		li=[]
		for i in range(0,len(a)-1):
			s=(a[i])**alpha1
			li.append(s)
		#print("list=",li)
		for i in range(0,len(li)-1):
			z+=li[i]
		#print("sum(z)=",z)
		r=1/alpha1
		h=z**r
		beta=h/n
		print("beta=",beta)
		k=int(input("Number of intervals(K):"))
		pj=1/k
		print("Pj(probability)=",pj) #probability
		Ej=n*pj
		print("Expected frequency=",Ej)
		ai=[]
		list1=[]
		ln_list=[]
		for i in range(0,k):
			l2=1-(i*pj)
			list1.append(l2)
		#print("ip=",list1)
		for d in range(0,len(list1)-1):
			ln_list.append(-log(list1[d]))
		for j in range(0,len(ln_list)-1):
			l=beta*((ln_list[j])**r)
			ai.append(l)
		#print("ai=",ai)
		oj_list=[]
		for i in range(0,len(ai)-1):
			cnt=0
			for j in range(0,len(a)-1):
				if (a[j]>=ai[i] and a[j]<ai[i+1]):
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
		
		for i in range(0,len(ui)):
			x=beta*((-log(1-(ui[i])))**r)
			xi.append(x)
		with open(filename,'w')as f:
			for item in xi:
				f.write("%s\n"% item)

	else:
		itr+=1
		#print("diff=",k)#find alpha upto till (next_alpha-prev_alpha=0.001)
		#print("____________________________________________________")
		fun(alpha1,itr)
fun(alpha0,itr)

