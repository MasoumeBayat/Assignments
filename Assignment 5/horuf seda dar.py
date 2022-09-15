text = input ('jomle ra vared konid : ')
listText = []
listSeda = ['i', 'o', 'u', 'e', 'a', 'I', 'O', 'U', 'E', 'A']
for letter in text :
    listText.append(letter)
for i in range (len(listText)):
    if listText[i] in listSeda :
        
        listText[i] = '?'
print(''.join(listText))