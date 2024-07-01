import random

def game():
    number_to_guess = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        attempts += 1
        if guess < number_to_guess:
            print("Too small!")
        elif guess > number_to_guess:
            print("Too large!")
    
    print(f"Congratulations! You found the number in {attempts} attempts.")

if __name__ == "__main__":
    game()