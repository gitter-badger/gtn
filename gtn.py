"""
Guess the number!
Generate X
+ or - while user doesn't win
You can select number of attempts
Easy = 5
Medium = 3
Hard = 1
"""

import random

print """\
*********************************
* Guess the number welcomes you!*
*                               *
*      You have 3 attempts!     *
*                               *
*          Let's go!            *
*********************************
"""

num = random.randrange(1,10)

print ("Enter your number:")
x = input()

if num > x:
    print ("It's bigger!")
    print num

if num < x:
    print ("It's smaller!")
    print num

if num == x:
    print ("You win!")
    print num
