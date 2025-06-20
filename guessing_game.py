import random

def number_guessing_game():
    best_score = None

    while True:   
        number = random.randint(1, 100)
        attempts = 0

        print("\nWelcome to the number guessing game!")
        print("Guess a number between 1 and 100:")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number:
                    print("Too low! Try again.")
                elif guess > number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed it in {attempts} attempts.")
                    
                    if best_score is None or attempts < best_score:
                        best_score = attempts
                        print("New best score!")
                    else:
                        print(f"Best score: {best_score} attempts")
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

        
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing!")
            break

number_guessing_game()
