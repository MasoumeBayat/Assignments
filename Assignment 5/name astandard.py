listAsami = []
for i in range(10) :
    esm=input('enter name')
    esm=esm.lower()    
    esm=esm[0].upper()+esm[1:]
    listAsami.append(esm)
    
print(listAsami)