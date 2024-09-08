import string
import random
from Super_Encryption_cheese import chars, key  # Import chars and key from the shared file

# Encryption
plain_text = input('Enter a message: ')
cipher_text = ''

for letter in plain_text:
    if letter in chars:
        index1 = chars.index(letter)
        cipher_text += key[index1]  # Map using the key
    else:
        cipher_text += letter  # Add non-alphabetic characters directly

print(f'Original message: {plain_text}')
print(f'Cipher message: {cipher_text}')

# Save the key and encrypted message to files
with open('encryption_key.txt', 'w') as f:
    f.write(''.join(key))  # Save the key as a string

with open('encrypted_message.txt', 'w') as f:
    f.write(plain_text + '\n')  # Save the plain text
    f.write(cipher_text + '\n')  # Save the cipher text
