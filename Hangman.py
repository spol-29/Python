import sys
import random
import math as mt
name = input("What is your name?\n")


def hangman_game():
    print(f"Hello, {name}, let's play hangman!")
    print("Start guessing...")
    bag_of_words = [
        "python",
        "machinelearning",
        "looping",
        "whileloop",
        "devops",
        "forloop",
        "deeplearning",
        "oops",
        "condition",
        "preprocessing",
        "modelling",
        "boulder",
        "bouncy",
        "bowling",
        "boxer",
        "bracelet",
        "brainstorm",
        "bucket",
        "buckle",
        "budget",
        "buffalo"
        "amnesia",
        "biology",
        "crystal",
        "drastic",
        "eloquent",
        "fantasy",
        "glacier",
        "hubcap",
        "imposter",
        "javelin",
        "kilogram",
        "lullaby",
        "monarchy",
        "narrator",
        "obstacle",
        "bittersweet",
        "curiosity",
        "dinosaur",
        "eternity",
        "flamingo",
        "genetics",
        "harmonious",
        "indulgent",
        "jester",
        "kangaroo",
        "liberty",
        "mysterious",
        "xylograph",
        "yielding",
        "zesty",
        "avalanche",
        "brilliant",
        "cosmic",
        "delightful",
        "ephemeral",
        "fireplace",
        "grateful",
        "hypnotic",
        "radiant",
        "serenity",
        "transparent",
        "ubiquitous",
        "verdant",
        "wistful",
        "xenophobia",
        "yesterday",
        "zucchini",
        "amplify",
        "bewilder",
        "luminous"
    ]
    word = random.choice(bag_of_words)
    guesses = " "
    turns = mt.ceil(len(word) * 1.35)
    word = word.lower()

    
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You win!")
            choice = input("Would you like to play again? y/n\n")
            if "y" in choice:
                hangman_game()
            elif "n" in choice:
                sys.exit()
            else:
                print("Something went wrong, type y or n.")
        guess = input("Guess a(one) character:")
        print(f"Number of turns left: {turns}")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong!")
            print(f"You have {turns} more guesses.")
            if turns == 0:
                print("You lose!")
                choice = input("Would you like to play again? y/n\n")
                if "y" in choice:
                    hangman_game()
                elif "n" in choice:
                    sys.exit()
                else:
                    print("Something went wrong, type y or n.")


hangman_game()