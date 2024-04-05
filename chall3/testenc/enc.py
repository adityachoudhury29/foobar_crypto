from Crypto.Util.number import *

with open('flag.txt') as file:
    FLAG = file.read().strip()

e = 65537
p = getPrime(512)
q = getPrime(512)
print(p)

n = p * q

m = bytes_to_long(FLAG.encode())

c = pow(m, e, n)

with open('chall.txt', 'w') as file:
    file.writelines([
        f'{n = }\n',
        f'{e = }\n',
        f'{c = }\n',
    ])
