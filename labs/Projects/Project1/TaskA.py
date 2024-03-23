def guess_number_game(low, high):

    print(f"Think of a number between {low} and {high}!")
    steps = 0  # Initialize the counter for the number of steps (guesses)

    # Main loop to perform the binary search
    while low <= high:
        # Calculate the midpoint of the current range as the next guess
        mid = (low + high) // 2

        # Inner loop to ensure the user provides a valid response
        while True:
            user_input = input(f"Is your number greater (>), equal (=), or less (<) than {mid}?\nPlease answer (<, =, >): ").strip()
            if user_input in ('<', '=', '>'):
                break  # Exit the inner loop if valid input is received
            else:
                # Prompt the user again if the input was invalid
                print("Error: Please enter a valid input (<, =, >).")
        
        steps += 1  # Increment the step counter after each guess
        if user_input == '=':
            # If the user confirms the guess, print success message and steps
            print("I have guessed it!")
            print(f"It took {steps} steps!")
            return
        elif user_input == '>':
            # Adjust the lower bound if the number is greater
            low = mid + 1
        else:  # user_input == '<'
            # Adjust the upper bound if the number is less
            high = mid - 1

        # If low surpasses high, it indicates inconsistent answers were given
        if low > high:
            print("Hmm, something doesn't add up. Are you sure about your answers?")
            return

# Range set from 1 to 100, but could be adjusted to any numbers
guess_number_game(1, 100)
