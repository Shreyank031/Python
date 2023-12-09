# Simple encode-decode project.
# Incomplete


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_no):
  new_word=""
  for letter in plain_text :
    position     = alphabet.index(letter)
    new_position = position + shift_no
    new_letter   = alphabet[new_position]
    new_word    += new_letter
  print(f"The encoded word is {new_word}")

def decrypt(encrypted_text,shift_no):
    decrypted_word = ""
    for letter in encrypted_text:
        position         = alphabet.index(letter)
        new_position     = position - shift_no
        decrypted_letter = alphabet[new_position]
        decrypted_word  += decrypted_letter
    print(f"The decrypted word is {decrypted_word}")
    
if direction == 'encode':
    encrypt(plain_text=text,shift_no=shift)
elif direction == 'decode':
    decrypt(encrypted_text=text,shift_no=shift)