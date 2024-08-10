def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        elif choice not in ('e', 'd'):
            print("Invalid choice, please try again.")
            continue

        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = encrypt(text, shift)
            print(f"Encrypted text: {result}")
        elif choice == 'd':
            result = decrypt(text, shift)
            print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()
