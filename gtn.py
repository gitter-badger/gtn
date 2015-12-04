import random


def play():
    """Contains the game process"""
    print("""\
    *************************************
    *  "Guess the number" welcomes you! *
    *                                   *
    *         Difficulty Levels:        *
    *                                   *
    *  1 - Easy (you have 5 attempts)   *
    *  2 - Normal (you have 3 attempts) *
    *  3 - Hard (you have 1 attempt)    *
    *                                   *
    *             Let's go!             *
    *************************************
    """)
    while True:
        try:
            diff = int(input("Select Difficulty Level: "))
        except ValueError:
            print("Wrong number!")
            continue
        else:
            if not (0 < diff < 4):
                print("Wrong number!")
                continue
            if diff == 1:
                attempt = 5
            elif diff == 2:
                attempt = 3
            elif diff == 3:
                attempt = 1
            break

    num = random.randrange(1, 10)
    x = 0

    while num != x:
        if attempt == 0:
            print("The number is", str(num) + ".")
            print("You lose.\n")
            return
        else:
            x = int(input("Enter your number: "))
            if num > x:
                print("It's bigger!\n")
            if num < x:
                print("It's smaller!\n")
            attempt -= 1

    print("The number is", str(num) + ".")
    print("You win!")


def game_over():
    """Ask user for replay or quit"""
    while True:
        restart = input("Would you like to play again? (y/n):\n")
        if restart == 'y':
            play()
        elif restart == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Wrong answer!")
            continue

if __name__ == "__main__":
    play()
    game_over()
