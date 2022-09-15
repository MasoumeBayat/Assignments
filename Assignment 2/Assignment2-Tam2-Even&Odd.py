number=float(input("please enter the number:"))
even=0
odd=0
while number>0:
 mod=number%10
 number=number//10
 if(mod%2==0):
     even+=1
 else:
     odd+=1
if(even==odd):
    print("number of odd equal with even.")
elif odd>even:
    print("number of odd is more than even. ")
else:
    print("number of even is more than odd.")