import itertools 
import string
import md5

alphabets = '0' + string.ascii_lowercase + '123456789'

for s in itertools.product(alphabets, repeat = 5):
    s = ''.join(s)
    print s
    r = str(int('0x' + md5.new(s).hexdigest(), 16))
    print r
    
    if '8705973470942652577929336993839061582' in r:
        print s
        print 'OK'
        break

