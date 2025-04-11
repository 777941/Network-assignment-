def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    encrypted_message = input("Enter the encrypted message: ")
    
    for shift_value in range(1, 27):
        decrypted_message = decrypt_caesar(encrypted_message, shift_value)
        print(f"Shift {shift_value}: {decrypted_message}")
