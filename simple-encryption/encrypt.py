import string
all_letters = string.ascii_letters

def encrypt(message):
    encrypted_message = ""
    for letter in message:
        if letter in all_letters:
            encrypted_letter = all_letters[(all_letters.index(letter)+1) % len(all_letters)]
            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter

    return encrypted_message

user_input = input("What to encrypt? ")
encrypted = encrypt(user_input)
print("Encrypted message: " + encrypted)