import random
import time
import math
from random import randint
from random import *

print("Addition guessing game")
print("----------------------------")
print("Startup Settings...")
print("----------------------------")
max1 = int(input("Please Choose a max number: "))
max2 = int(input("Please Choose another max number: "))
print("----------------------------")
answerz = int(input("What do you think the answer will be? "))
print("----------------------------")
print("That is the end of Startup Settings")
print("Thank You")
number1 = (randint(0, max1))
choice1 = (number1)
number2 = (randint(0, max2))
choice2 = (number2)
print("----------------------------")
sum1 = int(choice1)
sum2 = int(choice2)
print("The choosen numbers are" , sum1 , "and" , sum2)
print("----------------------------")
answer = (sum1 + sum2)
print(sum1 , "+" , sum2 , '=' , answer)
if answer==answerz:
    print('You Win!')
else:
    print("Unfortunately you lost")
print("----------------------------")
input("Press enter to exit")
