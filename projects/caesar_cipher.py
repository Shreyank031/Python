# Simple encode-decode project.
# Incomplete


# Define the alphabet as a list, including a shifted copy for handling wrapping
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

# Prompt the user for the encryption/decryption direction ('encode' or 'decode')
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# Take user input for the message to be encrypted or decrypted and convert it to lowercase
text = input("Type your message:\n").lower()

# Prompt for the shift number (key) to perform the encryption or decryption
shift = int(input("Type the shift number:\n"))

# Function to perform the Caesar cipher encryption/decryption
def caesar(start_text, shift_no, caesar_direction):
    new_word = ""  # Initialize an empty string to store the encrypted/decrypted word
    
    if caesar_direction == "decode":  # Reverse the shift direction for decryption
        shift_no *= -1

    for letter in start_text:  # Loop through each letter in the input text
        if letter in alphabet:  # Check if the letter is in the defined alphabet
            position = alphabet.index(letter)  # Find the index of the letter in the alphabet
            new_position = position + shift_no  # Shift the position by the specified amount
            new_letter = alphabet[new_position]  # Get the new letter based on the shifted position
            new_word += new_letter  # Append the new letter to the encrypted/decrypted word
        else:
            new_word += letter  # If the character is not in the alphabet, keep it unchanged
    
    print(f"The {caesar_direction} word is {new_word}")  # Print the result of encryption/decryption

# Call the caesar function with the provided inputs
caesar(start_text=text, shift_no=shift, caesar_direction=direction)

