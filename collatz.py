def collatz(number):
    """
    Calculates the next step in the Collatz sequence.

    If the number is even, it prints and returns number // 2.
    If the number is odd, it prints and returns 3 * number + 1.
    Each printed number is followed by a space to keep the output on one line.

    Args:
        number (int): The current integer in the Collatz sequence.

    Returns:
        int: The next integer in the Collatz sequence.
    """
    if number % 2 == 0:
        # If the number is even, divide by 2
        next_value = number // 2
    else:
        # If the number is odd, multiply by 3 and add 1
        next_value = 3 * number + 1

    # Print the next value, followed by a space, without a newline
    print(next_value, end=' ')

    return next_value


# --- Main Program ---

# Loop to get valid integer input from the user
while True:
    try:
        # Prompt the user to enter a number
        # Using '\n' after the prompt to match the example output's line break
        user_input = input("Enter number:\n")

        # Attempt to convert the input string to an integer
        user_number = int(user_input)

        # Collatz conjecture is typically for positive integers
        if user_number <= 0:
            print("Please enter a positive integer.")
            continue  # Go back to the start of the loop to ask for input again

        # If conversion is successful and number is positive, break out of the input loop
        break
    except ValueError:
        # If int() raises a ValueError (e.g., input was 'puppy'), print an error message
        print("You must enter an integer.")

# Print the starting number, followed by a space, to begin the sequence output on one line
print(user_number, end=' ')

# Keep calling the collatz() function until the number returns 1
while user_number != 1:
    # Call collatz() with the current number and update the number with the returned value
    user_number = collatz(user_number)

# After the loop finishes (i.e., user_number is 1), print a final newline
# This ensures that the next prompt or output starts on a new line.
print()
