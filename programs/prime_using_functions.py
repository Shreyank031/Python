# Define a function to check if a number is prime
def prime_checker(number):
    is_prime_no = True  # Initialize a flag to assume the number is prime initially

    # Iterate through numbers from 2 to number - 1 to check for factors
    for i in range(2, number):
        if number % i == 0:  # If the number is divisible by i without any remainder
            is_prime_no = False  # Set the flag to indicate that the number is not prime

    if is_prime_no:  # If the flag is still True after the loop
        print(f"The number {number} is prime")  # Print that the number is prime
    else:
        print(f"The number {number} is not prime")  # Print that the number is not prime

# Take user input for the number to be checked
num = int(input("Type the number to check: \n"))

# Call the prime_checker function with the user input number
prime_checker(number=num)
