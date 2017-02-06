The idea this time is to crack RSA built with small prime numbers. We first needed to find the public modulus *n* and then factorize it, since:

    n = p*q

Our code to do it:

~~~~
from Crypto.PublicKey import RSA
import gmpy
import base64
import binascii

with open('key.pub','r') as key:
    pub = RSA.importKey(key.read())

n = int(pub.n)

print(n)
~~~~

[FactorDB](http://factordb.com/) is the best place I know to do it and we got very quickly the results for *p* and *q*:

~~~~
# Using factordb
p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901
~~~~

Now we can rebuild the private key. Instead of doing the same thing we did with CR3, I tried to explore *gmpy* module:

~~~~
# We could also use the same algorithm we did with cr3
d = int(gmpy.invert(e,(p-1)\*(q-1)))
print(d)

pvt = RSA.construct((n, e, d, p, q))

print(pvt.exportKey().decode())
~~~~

And here it is:

~~~~
-----BEGIN RSA PRIVATE KEY-----
MIH5AgEAAjJSqZ4knufPPAy/ljoAlmF3K8nN9uHj+/xuRKB6Xg+JRFep+Bw64TKs
VoPTWyi6XDJCQwIDAQABAjIzrQnKBvUPnpCxrK5x85DWuS8dbTtmFP+HEYHE3wja
TF9QEkV6ZDCUBers1jQeQwJ5MQIaAImWgwYMdrnA3lgaaeDqnZG+0Qcb6x2SSjcC
GgCZzedK7e6Hrf/daEy8R451mHC08gaS9lJVAhlmZEB1y+i/LC1L27xXycIhqKPe
aoR6qVfZAhlbPhKLmhFavne/AqQbQhwaWT/rqHUL9EMtAhk5pem+TgbW3zCYF8v7
j0mjJ31NC+0sLmx5
-----END RSA PRIVATE KEY-----
~~~~

For some weird reason (which I did not take the time to figure out), python3 was complaining about a charachter when decoding the flag. So instead of struggling with it forever I decided to move on and give OpenSSL a try:

    base64 -d flag.b64 | openssl rsautl -decrypt -inkey key.pvt | cat
    ALEXCTF{SMALL_PRIMES_ARE_BAD}

This above simply decodes the base64 flag and uses openssl to decrypt it. And they sure do :)
