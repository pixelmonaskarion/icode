def flip_bits_in_string(input_string):
    # Convert the string to bytes
    input_bytes = input_string.encode('utf-8')
    
    # Flip all the bits in each byte
    flipped_bytes = bytearray(~byte & 0xFF for byte in input_bytes)
    
    return flipped_bytes

def encrypt(message):
    flipped_bytes = flip_bits_in_string(message)
    encrypted_hex = flipped_bytes.hex()
    return encrypted_hex

user_input = input("What to encrypt? ")
encrypted = encrypt(user_input)
print("Encrypted message: " + encrypted)