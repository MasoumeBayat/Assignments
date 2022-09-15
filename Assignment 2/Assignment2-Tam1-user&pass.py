username="Baran"
password=8013
counter=0
while (counter<3):
  name=input("please enter username:")
  pas=int(input("please enter the password:")) 
  if (name==username) and (pas==password):
    print("welcome")
    break
  else:
    print("username or password is incorrect.")
  counter=counter+1
if(counter>2):
    print("access denied!")