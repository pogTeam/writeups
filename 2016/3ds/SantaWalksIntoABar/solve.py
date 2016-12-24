import os
import qrtools

qr = qrtools.QR()
for idx, f in enumerate(os.listdir(".")):
    if "solve" in f:
        continue
    qr.decode(f)
    if "you" in qr.data:
        print "File content >> %s" % qr.data
        img = qr.data.rsplit(' ', 1)[1]+".png"
        qr.decode(img)
        print "      " + img + " >> " + qr.data
