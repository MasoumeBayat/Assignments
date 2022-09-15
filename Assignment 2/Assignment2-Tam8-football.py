totalPoints = 0
win=0
equal = 0
lose = 0 
Counter = 1
while (Counter <= 8):
    print ('enter the game point  :  win : 3  equal : 1  lose : 0  point ', Counter ,' : ')
    point = int(input())
    totalPoints += point
    Counter += 1
    if (point == 3):
        win += 1
    elif (point == 1):
        equal += 1
    elif (point == 0):
        lose += 1
print ('total points=' , totalPoints ,   'wins = ' , win,  'equal=' , equal,  'loses =', lose )