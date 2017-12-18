# Cappo di Tutti Cappo - 500 pts

~~~
Help the FBI

Server: capoditutticapi01.3dsctf.org

Port: 8001
~~~

Connecting with `nc`:

~~~
                +++     3DSCTF - Capo Di Tutti Capi     +++

[+] One year after the death of the one of the most famous members of the
mafia, the FBI found a notebook with a few weird annotations.

[+] Trying to use the same strategy as the last time, all the FBI experts
    failed to translate the book. Look if you have some luck!

[+] Type start to read the first note: start
Openning the book...

[+] Page 1/10 [c, r, p]: [ZNEKWSGQXYRMVUDHPBTILFCOJA, 5, SRJYC S ZUQJICK, OVSCLYT KIAC HTURY]
The answer is:                                    
~~~

Every round the challenge gave us 3 different elements in the same format:

    'NEHQAOBYXUGDZMPSKFRIJVWLCT', 2, 'VUB QBJV CHN VK BSVBI KWI QWJGSBJJ GJ VK QB QKIS GSVK GV'

The first element (`NEHQAOBYXUGDZMPSKFRIJVWLCT`) is always a 26 chars string, a strong indicator of a substitution alphabet. The second element (`2`) is always a number between 1 and 26, which seems like an offset. It could be related to a rotation, like in a Caesar Cipher. The last element is probably the encrypted message itself.

With these informations in mind we confirmed there were indeed both a substitution and a rotation involved. To decrypt, we first substituted back the message according to the alphabet, and then applied a rotation according to the offset.

The code below gave us what we needed:

~~~
import string
from pwn import *

def substitute(msg, alphabet):
    subs = {}
    for x,y in zip(alphabet, string.ascii_uppercase):
        subs[x] = y

    subs[' '] = ' '
    subs[','] = ','
    subs['.'] = '.'

    res = ''
    for c in msg:
        res += subs[c]

    return res

def rotate(msg, offset):
    res = ''
    for c in msg:
        if c == ' ':
            res += ' '
            continue
        elif c==',':
            res+=','
            continue
        elif c=='.':
            res+='.'
            continue
        elif ord(c)-ord('A')<offset:
            x = ord('A')-ord(c)
            res += chr(ord('Z')-(offset-1+x))
        else:
            res += chr(ord(c)-offset)
    return res

def parseRcv(rcv):
    splitRcv = rcv.split(',')
    alphabet = rcv[:26]

    if len(splitRcv[1].strip()) == 1:
        offset = int(rcv[28:29])
        msg = rcv[31:]
    elif len(splitRcv[1].strip()) == 2:
        offset = int(rcv.strip()[28:30])
        msg = rcv[32:]

    return alphabet, offset, msg


conn = remote('capoditutticapi01.3dsctf.org', 8001)
print(conn.recvuntil('note:'))
conn.send('start\n')

while 1:
    print(conn.recvuntil(':'))
    rcv = conn.recvline()[2:-2]
    print(rcv)
    rcv = parseRcv(rcv)
    print(rcv)

    alphabet = rcv[0]
    offset = rcv[1]
    msg = rcv[2]


    print(alphabet, offset, msg)
    sub = substitute(msg, alphabet)
    rot = rotate(sub, offset)

    print(rot)

    conn.send(rot+'\n')
    print(conn.recvline())
    print(conn.recvline())
~~~
