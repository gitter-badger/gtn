import random


def play():
    global attempt
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
            if diff < 0 or diff > 3:
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
    while True:
        restart = int(input("Would you like to play again? Please enter '1' for YES or '2' for NO: "))
        if restart == 1:
            play()
        else:
            print("Thanks for playing!")
            break


def main():
    play()
    game_over()

main()
