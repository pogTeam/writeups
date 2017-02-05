import re
import binascii

word = open('final.txt').read()
r = re.findall('([A-Z])', word)
print binascii.unhexlify('%x' % (int(''.join(r).replace('ZERO','0').replace('ONE','1'),2)))