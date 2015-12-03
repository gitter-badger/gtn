"""
Guess the number!
Generate X
+ or - while user doesn't win
"""

import random

print ("'Guess the number' welcomes you!")
print ("You have 3 attempts!")
print ("Let's go!")
num = random.randrange(1,10)

print ("Enter your number:")
x = input()

if num == x:
    print ("You win!")
    print num

if num > x:
    print ("It's bigger")
    print num

if num < x:
    print ("It's smaller")
    print num
