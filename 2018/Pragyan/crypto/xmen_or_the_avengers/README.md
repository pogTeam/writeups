# Xmen OR the avengers (100pts)

~~~
The legion of doom is expecting an impending attack from a group of superheroes. they are not sure if it is the Xmen OR the avengers. They have received some information from a spy, a zip file containing the following files:

info_crypt.txt

info_clear.txt

superheroes_group_info_crypt.txt

Help the legion of doom in decrypting the last file so they can prepare themselves and prevent their impending doom.
~~~

~~~
import base64
import hashlib
from Crypto.Cipher import AES

def readfile(path):
    with open(path, 'r') as f:
        return f.read()

def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

#read the files
clear = readfile('info_clear.txt')
crypt = readfile('info_crypt.txt')
superhero = readfile('superheroes_group_info_crypt.txt')
superhero = base64.b64decode(superhero)

#get the key
dec = xor(clear,crypt).rstrip('\n').encode('utf-8')
print(dec)
key = hashlib.md5(dec).hexdigest().encode()
print(key)

#decrypt aes-ecb
cipher = AES.new(key, AES.MODE_ECB)
msg = cipher.decrypt(superhero)
print("***POGTEAM*** >> " + msg)
~~~
