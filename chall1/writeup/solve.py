from Crypto.Cipher import AES
import random
from Crypto.Util.Padding import pad
from pwn import *
import time
from tqdm import tqdm
t = time.time()

dcts = set()
mems = {}
plaintext = b'a'
c1=b'05f50f9b5b90fa4133e8a30b9214413fde6972dca88f81dc314fa906d9ed009f'
c2=b'14d3eea21fc437619449b41a3af37ae6'
flagcip = bytes.fromhex(c1.decode())
cts = bytes.fromhex(c2.decode())

for i in range(999999):
    a = (str(i).zfill(6)*4)[:16].encode()
    cipher = AES.new(a, mode=AES.MODE_ECB)
    enc = cipher.encrypt(pad(plaintext, 16))
    dcts.add(enc)
    mems[enc] = i

print("Ones complete")

keya = -1
keyb = -1
for i in range(999999):
    a = (str(i).zfill(6)*4)[:16].encode()
    cipher = AES.new(a, mode=AES.MODE_ECB)
    dec = cipher.decrypt(cts)
    if(dec in dcts):
        print("Founds!!")
        keya = mems[dec]
        keyb = i
        break

print("Done!!")
aa = (str(keya).zfill(6)*4)[:16].encode()
bb = (str(keyb).zfill(6)*4)[:16].encode()
cipher1 = AES.new(bb, mode=AES.MODE_ECB)
ct = cipher.decrypt(flagcip)
cipher2 = AES.new(aa, mode=AES.MODE_ECB)
flag = cipher2.decrypt(ct)
print(flag)