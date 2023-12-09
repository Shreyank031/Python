# Define the alphabet as a list, including a shifted copy for handling wrapping
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',  
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
            't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo  # Importing logo from the art module
print(logo)  # Displaying the logo

# Function to perform Caesar cipher encryption/decryption
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""  # Initialize an empty string to store the resulting text
    if cipher_direction == "decode":
        shift_amount *= -1  # Reverse the shift direction for decryption
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)  # Find the position of the character in the alphabet
            new_position = position + shift_amount  # Shift the position by the specified amount
            end_text += alphabet[new_position]  # Append the new character to the result
        else:
            end_text += char  # If the character is not in the alphabet, append it unchanged
    print(f"Here's the {cipher_direction}d result: {end_text}")  # Display the encrypted/decrypted result

should_continue = True  # Flag to control continuation of the program
while should_continue: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26  # Ensure the shift value is within the range of the alphabet's length

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)  # Perform encryption/decryption

    result = input("Type 'yes' to continue or 'no' to exit:\n").lower()
    if result != "yes":
        should_continue = False  # Exit the loop if the user does not want to continue
        print("Goodbye")  # Display a goodbye message