def flip_bits_in_bytes(input_bytes):
    # Flip all the bits in each byte
    flipped_bytes = bytearray(~byte & 0xFF for byte in input_bytes)
    
    return flipped_bytes

def decrypt(encrypted_message):
    encrypted_bytes = bytes.fromhex(encrypted_message)
    flipped_bytes = flip_bits_in_bytes(encrypted_bytes)
    message = flipped_bytes.decode()
    return message

user_input = input("What to decrypt? ")
encrypted = decrypt(user_input)
print("Original message: " + encrypted)