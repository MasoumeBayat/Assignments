number=int(input('enter number :'))
if number%7==0:
    print('number is divisible by 7')
else:
   nextNumbers=(number+(7-(number%7)))
   print("next number that is divisible by 7 is",nextNumbers)