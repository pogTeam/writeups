from Crypto.PublicKey import RSA
import gmpy
import base64
import binascii

with open('key.pub','r') as key:
    pub = RSA.importKey(key.read())

n = int(pub.n)
e = int(pub.e)

print(n)
print(e)

# Using factordb

p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901

# We could also use the same algorithm we did with cr3
d = int(gmpy.invert(e,(p-1)*(q-1)))
print(d)

pvt = RSA.construct((n, e, d, p, q))

print(pvt.exportKey().decode())
flag = b"Ni45iH4UnXSttNuf0Oy80+G5J7tm8sBJuDNN7qfTIdEKJow4siF2cpSbP/qIWDjSi+w="
flag = base64.b64decode(flag)
print(flag)
flag = binascii.unhexlify(flag)
print(int(flag))

pt = pvt.decrypt(flag)

print(pt)
#print(binascii.unhexlify(pt[2:]))

