import binascii
import base64

with open('zero_one') as f:
        r = f.read().split()

        print '[+] Bin: ' + ''.join(r).replace('ZERO','0').replace('ONE','1')
        print '[+] B64: ' + str(binascii.unhexlify('%x' % (int(''.join(r).replace('ZERO','0').replace('ONE','1'),2))))
        print '[+] B64 Decode: ' + base64.b64decode(binascii.unhexlify('%x' % (int(''.join(r).replace('ZERO','0').replace('ONE','1'),2))))
