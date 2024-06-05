def rail_fence_cipher(text):
    encrypted_text = ''
    for i in range(len(text)):
        if i % 2 == 0:
            encrypted_text += text[i]
    for i in range(len(text)):
        if i % 2 == 1:
            encrypted_text += text[i]
    return encrypted_text


def rail_fence_decipher(text):
    length = len(text)
    if length % 2 == 0:
        k = length // 2
    else:
        k = (length // 2) + 1

    deciphered_text = ''
    for i in range(k):
        deciphered_text += text[i]
        if i + k < length:
            deciphered_text += text[i + k]

    return deciphered_text


def main():
    print("RAIL FENCE TECHNIQUE")
    text = input("Enter the input string: ")

    # Ciphering
    encrypted_text = rail_fence_cipher(text)
    print("Cipher text after applying rail fence: ", end='')
    print(encrypted_text)

    # Deciphering
    decrypted_text = rail_fence_decipher(encrypted_text)
    print("Text after decryption: ", end='')
    print(decrypted_text)


if __name__ == "__main__":
    main()