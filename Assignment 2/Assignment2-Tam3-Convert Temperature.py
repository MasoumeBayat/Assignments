F=0
C=0
K=0
while True:
    temperature=float(input("Please enter the temperature:"))                
    typeTemperature=input("Please enter type of temperature(F,C,K):") 
    conversion=input("What temperature do you want to convert?(F,C,K):")
    
    if(typeTemperature=='F') and (conversion=='C'):
        c=(temperature - 32) / 1.8
        print("Temperature based on Celsius is:",C)
    elif (typeTemperature=='C') and (conversion=='F'):
        F=(temperature * 1.8) + 32
        print("Temperature based on Fahrenheit is:",F)
    elif (typeTemperature=='F') and (conversion=='K'):
        K=((temperature + 459.67) / 1.8)      
        print("Temperature based on kelvin is:",K)
    elif (typeTemperature=='K') and (conversion=='F'):
        F=((temperature * 1.8) - 459.67)
        print("Temperature based on Fahrenheit is:",F)
    elif (typeTemperature=='K') and (conversion=='C'):
        c= temperature- 273.15
        print("Temperature based on Celsius is:",C)
    elif (typeTemperature=='C') and (conversion=='K'):
        K=temperature+ 273.15
        print("Temperature based on kelvin is:",K)
    else:
        print("Please try agin.")