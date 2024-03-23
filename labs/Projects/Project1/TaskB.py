def binary_search_guess(low, high, elements, element_type):
    steps = 0  # Initialize step counter
    while low <= high:
        steps += 1  # Increment step counter for each iteration
        mid = (low + high) // 2
        mid_element = elements[mid]  # Selecting the middle element

        # Specific case for guessing in a character array
        if steps == 1 and element_type == 'character':
            mid_element = 'M'  # Force 'M' for the first step

        # Prompt for user input with validation loop
        user_input = input(f"Is your {element_type} after (>), equal (=), or before (<) than the letter {mid_element}?\nPlease answer (<, =, >): ").strip()
        while user_input not in ('<', '=', '>'):
            print("Error: Please enter a valid input (<, =, >).")
            user_input = input(f"Is your {element_type} after (>), equal (=), or before (<) than the letter {mid_element}?\nPlease answer (<, =, >): ").strip()

        if user_input == '=':
            return mid_element, steps  # Successful guess
        elif user_input == '>':
            # Adjusting search range based on input, with special handling for 'M'
            low = elements.index('N') if mid_element == 'M' and steps == 1 else mid + 1
        else:
            # Adjusting search range based on input, with special handling for 'M'
            high = elements.index('M') - 1 if mid_element == 'M' and steps == 1 else mid - 1

    return None, steps  # In case of no successful guess

def guess_number_or_letter():
    # Generate number and letter lists for searching
    letters = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)]
    
    print("Think of a number between 1 and 100, or think of a character between A-Z or a-z!")

    # Attempt to guess the thought character first
    guessed, steps = binary_search_guess(0, len(letters)-1, letters, 'character')
    if guessed:
        print(f"I have guessed it! It's {guessed}.")
        print(f"It took {steps} steps!")
        return

    # Prints inconsistency if no guess was made
    print("Hmm, something doesn't add up. Are you sure about your answers?")
    if not guessed:
        print(f"No guess was made in {steps} steps. Please ensure your responses are consistent.")

guess_number_or_letter()
