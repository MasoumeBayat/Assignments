m=int(input('enter your round: '))
list=[]
for i in range(m):
    name=input("enter name:")
    list.append(name)
    m=list.count(list[i])
    print(m,'=',list[i])