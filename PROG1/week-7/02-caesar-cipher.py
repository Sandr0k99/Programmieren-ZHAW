def encrypt(char, shift):
    ascii_code = ord(char)
    new_code = 97 + ((ascii_code - 97 + shift) % 26)
    return chr(new_code)


def decrypt(encryption, cipher):
    ascii_code = ord(encryption)
    old_code = 97 + ((ascii_code - 97 - cipher) % 26)
    return chr(old_code)


char = (input("Character: ")).lower()
shift_by = int(input("Shift by: "))
new_char = encrypt(char, shift_by)
print(f"Encrypted Character: {new_char}")
print(f"Decrypted Character: {decrypt(new_char, shift_by)}")

