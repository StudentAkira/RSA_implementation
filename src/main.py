import random


def calc_pqe() -> tuple:
    n = 100
    divs = [True]*n
    for i in range(2, n):
        if divs[i]:
            for j in range(i*i, n, i):
                divs[j] = False
    divs[1] = False

    i = int(len(divs)/random.randint(1, 10)) % len(divs)
    while not divs[i] or i < n/2:
        i = (i + 1) % len(divs)
    p = i

    i = int(len(divs)/random.randint(1, 10)) % len(divs)
    while not divs[i] or i == p or i < n/2:
        i = (i + 1) % len(divs)
    q = i

    i = int(len(divs)/random.randint(1, 10)) % len(divs)
    while not divs[i] or i == p or i == q or i < n/2:
        i = (i + 1) % len(divs)
    e = i

    return (p, q, e)


def calc_d(e: int, T: int) -> int:
    i = 1
    d = (1 + i*T)/e
    while d - int(d) > 0.0001:
        i += 1
        d = (1 + i * T) / e
    return int(d)


def encrypt(message: str, public_key: tuple) -> str:
    encrypted_message = ''
    for i in message:
        encrypted_message += chr((ord(i)**public_key[0])%public_key[1])
    return encrypted_message


def decrypt(encrypted_message, private_key):
    message = ''
    for i in encrypted_message:
        message += chr((ord(i)**private_key[0])%private_key[1])
    return message


p, q, e = calc_pqe()
n = p*q
T = (p-1)*(q-1)
d = calc_d(e, T)

print('p :: ', p)
print('q :: ', q)
print('e :: ', e)
print('n :: ', n)
print('T :: ', T)
print('d :: ', d)

public_key = (e, n)
private_key = (d, n)

message = 'test'

encrypted_message = encrypt(message, public_key)
decrypted_message = decrypt(encrypted_message, private_key)

print('original : ', message)
print('encrypted : ', encrypted_message)
print('decrypted : ', decrypted_message)
