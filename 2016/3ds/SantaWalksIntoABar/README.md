~~~~
[EN]
Santa walks into a bar and creates a friendship bound with you.
After some shots, he spells to you his secrets to delivery all gifts on Christmas: he has a magical linked list that inform the next kiddie to visit.
At the end of the night, he goes alway and left behind his wallet and the bag with the list of gifts to delivery. Try to discover if you will receive something.

[PT-BR]
Papai noel entra em um bar e cria um laço de amizade com voce. 
Apos algumas bebidas, ele conta seu segredo para entregar todos os presentes de Natal: ele tem uma lista ligada que informa qual a porxima crianca que ele deve visitar. No final da noite, ele foi embora e esqueceu a carteira e a bolsa com a lista de presentes para entregar. Tente descobrir se voce ira receber alguma coisa.
~~~~

The given file is a *.zip* with lots of *.png* files within. Each file is a QR code that translates to a simple message indicating a name of a child. Our goal is to find the one addressed to us.

Althoug the chall mentions a linked list, there is indeed no need of it. Each translated QR code actually points to another file name, therefore we could simply run all the nodes of the list. However there are actually some few linked lists put toghether in this folder. If you start with a random node, say the first file in alphabetic order, you might end up with a message like "Fail!" being the last node of this list.

Instead of trying every possible list, we decided to simply check all files inside the folder sequentially. Nevertheless, we are still talking about a linked list anyhow :)

This silly script did the trick in a few minutes:

~~~~
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
~~~~

And the output:

~~~~
File content >> Next kiddie is you in 6f0600da67c1870c157d1f61e0c58091
      6f0600da67c1870c157d1f61e0c58091.png >> Yu u no following right?
File content >> A child in you in ed7b0eaaf64c9bf6c90299f6cbe6d4e1
      ed7b0eaaf64c9bf6c90299f6cbe6d4e1.png >> Fail
File content >> A kid called you in dec1eadad9056c9ebde333c90cfd3769
      dec1eadad9056c9ebde333c90cfd3769.png >> Ops!
File content >> A kid called you in 0a6d1cb51e224c3ad799fc91c9c5f68e
      0a6d1cb51e224c3ad799fc91c9c5f68e.png >> So wrong!
File content >> I almost forgot you in 3ab3b4b87d57315315cbb0259a262177
      3ab3b4b87d57315315cbb0259a262177.png >> Y0ur gift is in goo.gl/wFGwqO inugky3leb2gqzjanruw42yk
File content >> A child in you in 6fece9e2a5b49c07cdd7e8c3235ab724
      6fece9e2a5b49c07cdd7e8c3235ab724.png >> Wrong!
~~~~

There you go! Just check the address *https://goo.gl/wFGwqO* to get the flag:

    3DS{I_h0p3_th4t_Y0u_d1d_n0t_h4v3_ch4ck3d_OnE_by_0n3}
