import string
all_letters = string.ascii_letters

def decrypt(encrypted_message):
    message = ""
    for letter in encrypted_message:
        if letter in all_letters:
            decrypted_letter = all_letters[(all_letters.index(letter)-1) % len(all_letters)]
            message += decrypted_letter
        else:
            message += letter

    return message

user_input = input("What to decrypt? ")
encrypted = decrypt(user_input)
print("Original message: " + encrypted)