import math

p = 3
q = 7
n = p * q

phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    else:
        e += 1

k = 2
d = ((k * phi) + 1) / e

print("n =", n)
print("e =", e)
print("d =", d)

print(f'Public key: {e, n}')
print(f'Private key: {d, n}')

msg = 11

C = pow(msg, e)
C = math.fmod(C, n)

M = pow(C, d)
M = math.fmod(M, n)

print(f'Original message:{msg}')
print(f'Encrypted message: {C}')
print(f'Decrypted message: {M}')
