counter=1
sum=0
numberOfUses=int(input('chand bar estefade mikonid?'))
import math
basicOrAdvance=input('az kodam ghesmat mashin hesab mikhahid estefade konid:\n1.basic\n2.advanced\n')
for i in range(numberOfUses) :
 if(basicOrAdvance=='1' or basicOrAdvance=='basic' ):
   print('az kodam amalgar estefade mikonid\n1.jam or +\n2.tafrigh or -\n3.zarb or *\n4.tahgsim or /\n5.taghsim sahih or //')
   print('6.mod or %/\n7.ghadremotlagh or ||\n8.tavan 2 or ^2 or **\n9.tavan or ^\n10.sin\n11.cos\n12.tan\n13.cotan')
   print('14.jzr or radical\n15.add aval')
   typeUse=input()
   if(typeUse=='+' or typeUse=='jam' or typeUse=='1' ):
     while True:
       num=(input('add ra vared konid dar payan "=" ra bezanid : '))
       if num=='=':
         print('hasel barbar ast ba :',sum)
         break
       number=float(num)
       sum+=number
   elif(typeUse=='-' or typeUse=='tafrigh' or typeUse=='2'):
      while True:
        b=1
        num2=input('add ra vared konid dar payan "=" ra bezanid :')
        if num2=='=':
          print('hasel barbar ast ba :',sum)
          break
        number2=float(num2)
        if b==1:
          sum=number2
          b=10
        else:
         sum-=number2
   elif(typeUse=='*' or typeUse=='zarb' or typeUse=='3'):
     sum=1
     while True:
        num3=input('add ra vared konid va sepas "=" ra bezanid :')
        if num3=='=':
          print('javab :',sum)
          break
        number3=float(num3)
        sum*=number3
   elif(typeUse=='/' or typeUse=='taghsim' or typeUse=='4'):
      a=1
      while True:
       num=input('add ra vared konid dar payan "=" ra bezanid :')