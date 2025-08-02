import random

def choose_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")
    
    while True:
        try:
            choice = int(input("Enter 1, 2, or 3: "))
            if choice == 1:
                return 50, 15, "Easy"
            elif choice == 2:
                return 100, 10, "Medium"
            elif choice == 3:
                return 200, 7, "Hard"
            else:
                print("Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")

def calculate_score(attempts, max_attempts, max_number):
    # Score: (remaining attempts / max attempts) * 1000 + bonus for smaller range
    remaining = max_attempts - attempts
    base_score = (remaining / max_attempts) * 1000
    range_bonus = (200 / max_number) * 100  # Smaller ranges give higher bonus
    return round(base_score + range_bonus)

def number_guessing_game():
    while True:
        # Get difficulty settings
        max_number, max_attempts, difficulty = choose_difficulty()
        
        # Generate a random number
        secret_number = random.randint(1, max_number)
        attempts = 0
        
        print(f"\nWelcome to the Number Guessing Game ({difficulty})!")
        print(f"I'm thinking of a number between 1 and {max_number}. You have {max_attempts} attempts.")

        while attempts < max_attempts:
            try:
                # Get user's guess
                guess = int(input("Enter your guess: "))
                attempts += 1

                # Validate guess is within range
                if guess < 1 or guess > max_number:
                    print(f"Please enter a number between 1 and {max_number}.")
                    continue

                # Check if guess is correct
                if guess == secret_number:
                    score = calculate_score(attempts, max_attempts, max_number)
                    print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                    print(f"Your score: {score}")
                    break
                elif guess < secret_number:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
                
                # Show remaining attempts
                print(f"Attempts remaining: {max_attempts - attempts}")
            
            except ValueError:
                print("Please enter a valid number.")
                continue

        if attempts >= max_attempts and guess != secret_number:
            print(f"\nGame Over! The number was {secret_number}.")
            print("Your score: 0")

        # Play again option
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    number_guessing_game()