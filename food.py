list=[]
while True:
    count=0
    total=0
    xdiff=0
    
    a=int(input())
    list.append(a)
    total+=a
    count+=1
    xaverage=total/count
    xdiff+=(xaverage-a)
    if a== 999:
        break
list2=[]
while True:
    count2=0
    total2=0
    ydiff=0
    
    b=int(input())
    list2.append(b)
    total2+=b
    count2+=1
    yaverage=total2/count2
    ydiff+=(yaverage-b)
    if b==999:
        break

for i in list[2]:
    print(i)






