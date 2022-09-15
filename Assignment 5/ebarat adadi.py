
text = input('abart ra vared konid : ')
amalgar = ['*','/','+','-']
listAmalgar = []
counter = 0

for letter in text :
    for i in range(4):
        if letter == amalgar[i]:
            listAmalgar.append(letter)

for i in range(4):
    listEbarat = text.split(amalgar[i])
    text = ' '.join(listEbarat)
listEbarat = text . split(' ')

while ''in listEbarat :
    listEbarat.remove('')

for i in range(len(listEbarat)):
    listEbarat[i] = int (listEbarat[i])

while '*' in listAmalgar  or  '/' in listAmalgar:
    if listAmalgar[counter] == '*':
        listEbarat[counter] = listEbarat[counter] * listEbarat[counter+1]
        listEbarat.pop(counter+1) 
        listAmalgar.pop(counter)
        counter -= 1

    elif listAmalgar[counter] == '/':
        listEbarat[counter] = listEbarat[counter]/listEbarat[counter+1]
        listEbarat.pop(counter+1) 
        listAmalgar.pop(counter)
        counter -= 1
    counter += 1
counter = 0 

while '+' in listAmalgar  or  '-' in listAmalgar:   
    if listAmalgar[counter] == '+':
        listEbarat[counter] = listEbarat[counter]+listEbarat[counter+1]
        listEbarat.pop(counter+1) 
        listAmalgar.pop(counter)
        counter -= 1
        
    elif listAmalgar[counter] == '-':
        listEbarat[counter] = listEbarat[counter]-listEbarat[counter+1]
        listEbarat.pop(counter+1) 
        listAmalgar.pop(counter)
        counter -= 1
    counter += 1 
print('hasel abarat barabar ast ba : ',listEbarat[0])
    