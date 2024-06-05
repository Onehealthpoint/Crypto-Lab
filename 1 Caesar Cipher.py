def encrypt(plain_text: str, key: int) -> str:
    cipher_text = ''
    for char in plain_text:
        if char.isupper():
            cipher_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            cipher_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            cipher_char = char
        cipher_text += cipher_char

    return cipher_text


def decrypt(cipher_text: str, key: int) -> str:
    plain_text = ''
    for char in cipher_text:
        if char.isupper():
            plain_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.islower():
            plain_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            plain_char = char
        plain_text += plain_char

    return plain_text


if __name__ == '__main__':
    plain_text = 'I am Sadik Karki'
    key = 23
    cipher_text = encrypt(plain_text, key)
    print(f'Plain text: {plain_text}')
    print(f'Key: {key}')
    print(f'Cipher text: {cipher_text}')
    print(f'Decrypted text: {decrypt(cipher_text, key)}')
