import random

# generates a random number in the rango of 1-100
num_to_guess = random.randint(1,100)
attempts = 0
print("Welcome To Guess-My-Num Game ! \nGuess The Number Between 1-100 I Chose.\n")

# main logic and game loop
while True:
    try : 
        guess = int(input(f"Guess ({10-attempts} attempts remaining): "))
        attempts += 1
        if guess == num_to_guess :
            print(f"\nCongratulations ! You Guessed Correct Number In {attempts} Attempts Out Of 10.")
            print("\nThanks For Playing !")
            break
        elif guess > num_to_guess :
            print("\nToo High !")
        else:
            print("\nToo Low !")
        if attempts == 10 :
            print("You've used all of your 10 attempts.")
            print("\nThanks For Playing !")
            break
    except ValueError:
        print("\nPlease Enter A Valid Input ! (Integers In The Range Of 1-100.)\n")
        continue
