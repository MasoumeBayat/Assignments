text = input('enter the word : ')
listText = []
listRtext = []
for letter in text :
    listText .append(letter)

while  ' ' in listText :
    listRtext.remove(' ')

for i in range(len(listText)):
    listRtext.append(listText[-i-1])

if listText == listRtext :
    print (' the word is palindorme')

else :
    print (' the word is not palindorme')