m=867
c=48
a=3
z1=1
ui=[]
number=int(input("Enter Number :"))
def ui_generator(z1):
    for i in range(0,number):
        zi=(z1*a+c)%m
        u=zi/m
        ui.append(u)
        z1=zi
   # print("ui=",ui)
 #   print("lenght=",len(ui))
ui_generator(z1)
