import random 
import time
import datetime

def rules():
    print("$$$$$$$$$$$$$$$$$ THERE ARE 7 RULES $$$$$$$$$$$$$$$$")
    print("1. LIMITED CHANCES")
    print("2. HINT WILL BE PROVIDED")
    print("3. YOU CAN CHOOSE THE RANGE  OR IF YOU WANT TO PLAY DEFAULT RANGE(1-100)")
    print("4. YOU CAN CHOOSE THE NUMBER OF CHANCES")
    print("5. YOU CAN CHOOSE THE TIME LIMIT")
    print("6. YOU CAN CHOOSE THE HINT TYPE")
    print("7. YOU CAN CHOOSE THE NUMBER OF PLAYERS")
    print("$$$$$$$$$$$$$$$$$ ENJOY THE GAME $$$$$$$$$$$$$$$$")
    print("$$$$$$$$$$$$$$$$$ HAVE FUN $$$$$$$$$$$$$$$$")
    print()

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("Let's start by reviewing the rules of the game:")
    rules()
    
    range_start= int(input("Enter the stating number of the range(or press Enter for default 1): ") or 1)
    range_end = int(input("Enter the ending number of the range(or press Enter for default 100): ") or 100)
    chances = int(input("Enter the number of chances you want (or press Enter for default 5): ") or 5)
    time_limit = int(input("Enter the time limit in seconds (or press Enter for default 30 seconds): ") or 30)

    secret_number=random.randint(range_start,range_end)

    print(f"Secret number is between {range_start} and {range_end}. You have {chances} chances to guess it.")

    while True:
        start_time = time.time()
        for attempt in range(1, chances + 1):
            guess = int(input(f"Attempt {attempt}/{chances}: Enter your guess: "))
            elapsed_time = time.time() - start_time
            
            if elapsed_time > time_limit:
                print("Time's up! You took too long to guess.")
                return
            
            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempt} attempts.")
                return
        
        print(f"Sorry, you've used all your chances. The secret number was {secret_number}.")
        return



if __name__ == "__main__":
    play_game()
    print("Thank you for playing the Number Guessing Game!")
    print("Goodbye!")