F=open("data.dat","r")
while(True):
    data=F.readline()
    if(data==""):break
    DL=data.split(",")
    DL[2]=DL[2].rstrip("\n")
    DL.append(int(DL[2])*20/100)
    print(DL)
F.close()
