height = float(input("Please Enter your height in meters :"))
weight = float(input("Please Enter your weight in kilograms :"))
BMI = weight / (height ** 2)
print("The BMI = ",BMI)
if  BMI <= 16 :
    print("shoma laghari shadid darid \n nasihat : hatman be pezeshk morajee kon ")
elif 16 < BMI < 18.5 :
    print ("shoma kahesh vazn darid  \n nasihat :talash kon ghazahaye salem ama por hajm bishtari bokhirid.")
elif 18.5 < BMI < 24 :
    print ("vazn shoma normal ast :) \n nasihat : ba varzesh hamin ra hefz kon.")
elif 24 < BMI < 30 :
    print ("shoma ezafe vazn darid \n nasihat : talash kon ba varzesh be vazn ideal beresi.")
elif 30 < BMI < 35 :
    print ("shoma chaghi daraje 1 darid \n nasihat : varzesh kon va rezhim bgir.")
elif 35 < BMI < 40 :
    print("shoma chaghi daraje 2 darid \n nasihat : shadidan varzesh kon va rezhim ghazaye khas khodet ra dashte bash.")
else :
    print("shoma chaghi daraje 3 darid \n nasihat : salamati shoma dar khatar ast hatma be pzeshk morajee kon")