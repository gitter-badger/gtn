import random

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
    lvl = input("Select Difficulty Level: ")
    if lvl == 1:
        lvl = 5
    elif lvl == 2:
        lvl = 3
    elif lvl == 3:
        lvl = 1

    num = random.randrange(1,10)
    x = 0

    while num != x:
        if lvl == 0:
            print ("You lose.\n")
#            gameover()
            return
        else:
            x = input("Enter your number: ")
            if num > x:
                print ("It's bigger!\n")
            if num < x:
                print ("It's smaller!\n")
            pass
            lvl = lvl - 1

    print ("You win!")
    print num

def gameover():
    while True:
        restart = input("Would you like to play again? Please enter '1' for YES or '2' for NO: ")
        if restart==1:
            play()
        else:
            print "Thanks for playing!"
            break

def main():
    play()
    gameover()

main()
