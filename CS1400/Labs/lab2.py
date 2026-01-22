import math# math.pi 처럼 math. + 명령어 해야함
from math import pi # <- math. 못붙임
from math import * # math. 안쓰고 그냥 명령어만 쓸수잇게. 위랑 같음

import random
#print(random.randint(1,100)) #random int, (a<= n <=b)
#random.randrange(1,100)  #random range, but not include right (a<= n <b)

#repeat(12) #not a syntax
#while(12) # choosing type of boolean
#for count in range(12) # 0 to 11, 12 counts.
#for count in range(1,12) #1 to 11, not including 12 -> 11 counts.

#total = 0
#average = 0
#for count in range(1000000)
    #total += random.randint(0,10)
    #average = total/1000000
    #print(average)

print("Welcome to Guessing Game! let's guess the number betwwen 1 to 6")

for irr in range(12):
    player_guess = int(input("enter the number between 1 to 6: "))
    random_number = random.randint(1, 6)
    if player_guess < 1 or player_guess > 6:
        print("Your number is not vaild. try again")
    else:
        print(f"your number: ",player_guess, ", and computer's number: ",random_number)
print("Finishing guessing game!")