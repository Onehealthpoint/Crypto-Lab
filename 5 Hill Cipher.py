def matrix_mul(mat1, mat2):
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[i] += mat1[i][j] * mat2[j]
        result[i] %= 26
    return result


def main():
    # Define the encryption matrix
    a = [
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ]

    # Define the decryption matrix
    b = [
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ]
    msg = input("Enter plain text (3 characters): ").upper()
    c = [ord(char) - 65 for char in msg]
    print("Numerical values of the plaintext:", c)
    d = matrix_mul(a, c)
    print("Encrypted Cipher Text:", ''.join(chr(num + 65) for num in d))
    decrypted = matrix_mul(b, d)
    print("Decrypted Cipher Text:", ''.join(chr(num + 65) for num in decrypted))


if name == "main":
    main()