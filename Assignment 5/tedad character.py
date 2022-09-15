text = input('enter the sentence : ')
numberLetter = 0
numberWord = 0
counter = 0

for letter in text:
    
    if  ('a' <= letter <= 'z')  or  ('A' <= letter <= 'Z'):
        numberLetter += 1
        counter    += 1
        if counter == 2:
            numberWord+=1
        continue

    else:
        
        counter = 0
numberCharacter = len (text)   
numberEnterSpace = text.count('\n') + text.count(' ')
numberPointComma = text.count(',') + text.count('.')
print('number_character =',numberCharacter,'\nnumber_letter ='
,numberLetter,'\nnumber_word =',numberWord)
print('number_enter_space =',numberEnterSpace,
'\nnumber_point_comma',numberPointComma)