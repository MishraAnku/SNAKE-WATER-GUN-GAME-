#-------------------------------------------------------------------------------------------------------------------------- SNAKE , WATER , GUN GAME

#  we all have played snake , water , gun game in our childhood.  
# write a python program which is capable of playing a game with the user .

import random

def swg(comp,mine):
    if(comp=='s' and mine=='g'):
        return True
    elif (comp=='w' and mine=='s'):
        return True
    elif (comp=='g' and mine=='w'):
        return True
    else:
        return False 
    
choice=('s','w','g')
comp=random.randint(0,2)
comp=choice[comp]
mine=input("choose either s , w or g")

win=swg(comp,mine)
print("you choose{mine}and the computer choose {comp}")
if win is None:
        print("match drawn")
if win:
        print("you won")
else:
        print("you lose")   
        