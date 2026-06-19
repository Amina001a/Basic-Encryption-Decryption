def encrypt(text, shift):
    encrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            encrypted += new_char

        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            decrypted += new_char

        else:
            decrypted += char

    return decrypted


print("ENCRYPTION & DECRYPTION ( CEASER cipher )")

message = input("Enter message: ")

shift = int(input("Enter shift key: "))

encrypted_text = encrypt(message, shift)

decrypted_text = decrypt(encrypted_text, shift)

print("\noriginal message :", message)
print("encrypted message:", encrypted_text)
print("decrypted message:", decrypted_text)