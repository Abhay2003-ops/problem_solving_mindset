#created a basic game using while loop
# The game will generate a random number between 1 and 10.
# The player will have to guess the number.
# The game will provide hints if the number is too high or too low.
# The game will end when the player guesses the correct number or chooses to quit.
# The game will display the number of attempts made by the player.
# The game will display a message when the game ends.
secret_number = 7  

attempts = 0


game_active = True


while game_active:
    print(f"\nAttempt {attempts + 1}:")
    user_input = input("Guess the number (between 1 and 10) or type 'q' or 'quit' to exit: ")

    if user_input.lower() in ["q", "quit"]:
        print("You chose to quit the game. Goodbye!")
        game_active = False  
    else:
        try:
        
            guess = int(user_input)
          
            attempts += 1

         
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                game_active = False  
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number or 'q'/'quit' to exit.")

print("Game Over.")

