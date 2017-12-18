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
