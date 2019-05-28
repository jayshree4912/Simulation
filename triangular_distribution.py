from sample_ui import*
import math
x1=[]
filename="triangular_dist_data.csv"
for i in range(0,len(ui)):
    if ui[i]<=0.5:
        h=math.sqrt(2*ui[i])
        x1.append(h)
    else:
        k=2-(math.sqrt(2*(1-ui[i])))
        x1.append(k)
with open(filename,'w') as f:
    for i in x1:
        f.write("%s\n"%i)
