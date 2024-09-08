from Super_Encryption_cheese import chars, max_attempts

# Load the key from a file
with open('encryption_key.txt', 'r') as f:
    key = list(f.read().strip())  # Read the key and convert to a list

# Load plain_text and cipher_text from the file
with open('encrypted_message.txt', 'r') as f:
    plain_text = f.readline().strip()  # First line is the plain text
    original_cipher_text = f.readline().strip()  # Second line is the cipher text

# Decryption
attempts = 0

while attempts < max_attempts:
    cipher_text = input('Enter cipher message: ').strip()  # Strip any extra spaces/newlines
    plain_text_decrypted = ''
    incorrect = False

    # Decrypt the message
    for letter in cipher_text:
        if letter in key:
            index1 = key.index(letter)  # Find the index of the letter in key
            plain_text_decrypted += chars[index1]  # Use the same index to find the corresponding letter in chars
        elif letter.isspace():  # Check if it's a whitespace character
           plain_text_decrypted += letter
        else:
            incorrect = True
            break

    # Debugging print statements
    print(f"Original plain text: {plain_text}")
    print(f"Decrypted text: {plain_text_decrypted}")
    print(f"Entered cipher text: {cipher_text}")

    # Check if decryption was successful
    if incorrect or plain_text_decrypted != plain_text:
        attempts += 1
        print(f'Incorrect cipher message! Attempts left: {max_attempts - attempts}')
    else:
        print(f'Original message successfully decrypted: {plain_text_decrypted}')
        break

# If the user exceeds the limit
if attempts == max_attempts:
    print('Your limits are expired!!!')
