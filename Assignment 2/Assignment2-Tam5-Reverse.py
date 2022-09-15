number = float(input("Please enter the number : "))
number1 = number
number2 = 0 
while number > 0 :
    number2 = (number2 * 10) + (number % 10)
    number = number //  10
print(" Reverse of number= ",number2)
if number1 == number2 :
    print("The number is equal to it's reverse. ")
else :
    print("The number is not equal to it's reverse. ")