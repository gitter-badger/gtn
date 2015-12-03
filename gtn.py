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
import sys

def play():
    print """\
    ************************************
    * "Guess the number" welcomes you! *
    *                                  *
    *        Difficulty Levels:        * 
    *                                  *
    *  1 - Easy (you have 5 attempt)   *
    *  2 - Normal (you have 3 attempt) *
    *  3 - Hard (you have 1 attempt)   *
    *                                  *
    *             Let's go!            *
    ************************************
    """
#   print ("Select Difficulty Level:")
#   dif = input()
    
    num = random.randrange(1,10)
    x = 0
    
    while num != x:
        print ("Enter your number:")
        x = input()
        if num > x:
            print ("It's bigger!\n")
        if num < x:
            print ("It's smaller!\n")
        pass
    
    print ("You win!")
    print num

def main():
    play()
    while True:
        restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")
        if restart==1:
            play()
        else:
            print "Thanks for playing!"
            break
main()
