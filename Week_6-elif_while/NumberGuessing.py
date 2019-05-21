#!/usr/bin/env python3

import random

def guess_computer_number():
    print("\n==Guess computer number==\n" \
          "In this game I will take a number from 1 to 100, and\n" \
          "you will try to guess it. You will be given 5 tries. The\n" \
          "lesser number of tries, the better. You may exit the game\n" \
          "anytime by keying in '-1'. Let's go!\n")
    compNo = random.randint(1, 100)
    attempt = 1
    guessedCorrectly = False

    while attempt <= 5:
        guessed = int(input("Try " + str(attempt) + ": "))

        if guessed < 0:
            break
        elif guessed < compNo:
            print(guessed, "is too low. Try again.")
        elif guessed > compNo:
            print(guessed, "is too high. Try again.")
        else:
            guessedCorrectly = True
            break

        attempt += 1

    if guessedCorrectly:
        print("Indeed! My number is", compNo)
    else:
        print("Boohoo, wrong! My number is", compNo)

def guess_my_number():
    print("\n==Guess my number==\n" \
          "In this game you will take a number from 1 to 100, and\n" \
          "I will try to guess it. Tell me if:\n" \
          " - I guessed correctly ('c')\n" \
          " - My guess is too high ('h')\n" \
          " - My guess is too low ('l')\n" \
          "You may exit the game anytime by keying in 'e'. Let's go!\n")

    lowest = 1
    highest = 100
    guessNo = random.randint(lowest, highest)
    tries = 0

    while True:
        status = input(str(guessNo) + "? [c, h, l] ").strip()
        tries += 1
        if status == 'c':
            break
        elif status == 'h':
            highest = guessNo
        elif status == 'l':
            lowest = guessNo
        elif status == 'e':
            return
        else:
            continue
        if highest - lowest <= 1:
            break
        guessNo = random.randint(lowest + 1, highest - 1)

    print("Your number is", guessNo, end = '')
    print(" (...and I guessed it in", tries, "tries)" if tries > 1 else "try)")

def __main():
    print("Hello & welcome to the number guessing game!\n" \
          "Select one of the following games to start:")
    print("1. Guess the computer\n2. Guess my number")
    gameNo = int(input("Enter game number: "))

    if gameNo == 1:
        guess_computer_number()
    elif gameNo == 2:
        guess_my_number()
    else:
        print("Invalid game number!!")
        return

    print("Game exiting... Did you have fun?")

if __name__ == "__main__":
    __main()
