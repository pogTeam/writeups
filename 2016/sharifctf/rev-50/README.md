# Getit

## Description
Open and read the flag file!

## Solution

After download the getit file we need to take a look what kind of file we are working on.
```bash
file getit
getit: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.24, BuildID[sha1]=e389cd7a4b9272ba80f85d7eb604176f6106c61e, not stripped
```

Let's run the file
```
./getit
```

We got any return, so let's check the file with the strings command
```bash
strings getit
/lib64/ld-linux-x86-64.so.2
libc.so.6
fopen
__stack_chk_fail
strlen
fseek
fputc
fclose
remove
fprintf
__libc_start_main
__gmon_start__
GLIBC_2.4
GLIBC_2.2.5
fffff.
/tmp/flaH
g.txf
[]A\A]A^A_
;*3$"
c61b68366edeb7bdce3c6820314b7498
SharifCTF{????????????????????????????????}
*******************************************
[...]
```

So we got some kind of string about the flag in hex above the SharifCTF line but it does not work, another interesting thing we have in the output is the /tmp/flaHg.txf, so let's check the calls
```bash
ce ./getit
__libc_start_main(0x400756, 1, 0x7ffdc20a5348, 0x4008f0 <unfinished ...>
strlen("c61b68366edeb7bdce3c6820314b7498"...)                                                                                                                   = 32
strlen("c61b68366edeb7bdce3c6820314b7498"...)                                                                                                                   = 32
strlen("c61b68366edeb7bdce3c6820314b7498"...)                                                                                                                   = 32
[...]
fopen("/tmp/flag.txt", "w")                                                                                                                                     = 0x144b010
fprintf(0x144b010, "%s\n", "********************************"...)                                                                                               = 44
strlen("SharifCTF{b70c59275fcfa8aebf2d59"...)                                                                                                                   = 43
fseek(0x144b010, 30, 0, 30)                                                                                                                                     = 0
fputc('5', 0x144b010)                                                                                                                                           = 53
fseek(0x144b010, 0, 0, 0)                                                                                                                                       = 0
fprintf(0x144b010, "%s\n", "********************************"...)                                                                                               = 44
strlen("SharifCTF{b70c59275fcfa8aebf2d59"...)                                                                                                                   = 43
fseek(0x144b010, 24, 0, 24)                                                                                                                                     = 0
fputc('a', 0x144b010)                                                                                                                                           = 97
fseek(0x144b010, 0, 0, 0)                                                                                                                                       = 0
[...]
fputc('{', 0x144b010)                                                                                                                                           = 123
fseek(0x144b010, 0, 0, 0)                                                                                                                                       = 0
fprintf(0x144b010, "%s\n", "********************************"...)                                                                                               = 44
strlen("SharifCTF{b70c59275fcfa8aebf2d59"...)                                                                                                                   = 43
fclose(0x144b010)                                                                                                                                               = 0
remove("/tmp/flag.txt")                                                                                                                                         = 0
+++ exited (status 0) +++
```

As we can see above we have the fopen function to a /tmp/flag.txt file, but in the end of the output we have the remove function to get rid of the file. So let's open the file into the gdb
```
gdb -q
(gdb) file getit
Reading symbols from getit...(no debugging symbols found)...done.
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
   0x0000000000400756 <+0>:	push   rbp
   0x0000000000400757 <+1>:	mov    rbp,rsp
   0x000000000040075a <+4>:	push   rbx
   0x000000000040075b <+5>:	sub    rsp,0x38
   0x000000000040075f <+9>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000400768 <+18>:	mov    QWORD PTR [rbp-0x18],rax
   0x000000000040076c <+22>:	xor    eax,eax
   0x000000000040076e <+24>:	mov    DWORD PTR [rbp-0x40],0x0
   0x0000000000400775 <+31>:	mov    eax,DWORD PTR [rbp-0x40]
   0x0000000000400778 <+34>:	movsxd rbx,eax
   0x000000000040077b <+37>:	mov    edi,0x6010a0
   0x0000000000400780 <+42>:	call   0x4005e0 <strlen@plt>
   0x0000000000400785 <+47>:	cmp    rbx,rax
   0x0000000000400788 <+50>:	jae    0x4007c7 <main+113>
   0x000000000040078a <+52>:	mov    eax,DWORD PTR [rbp-0x40]
   0x000000000040078d <+55>:	lea    edx,[rax+0xa]
   0x0000000000400790 <+58>:	mov    eax,DWORD PTR [rbp-0x40]
   0x0000000000400793 <+61>:	cdqe
   0x0000000000400795 <+63>:	movzx  eax,BYTE PTR [rax+0x6010a0]
   0x000000000040079c <+70>:	mov    ecx,eax
   0x000000000040079e <+72>:	mov    eax,DWORD PTR [rbp-0x40]
   0x00000000004007a1 <+75>:	and    eax,0x1
   0x00000000004007a4 <+78>:	test   eax,eax
   0x00000000004007a6 <+80>:	je     0x4007af <main+89>
   0x00000000004007a8 <+82>:	mov    eax,0x1
   0x00000000004007ad <+87>:	jmp    0x4007b4 <main+94>
   0x00000000004007af <+89>:	mov    eax,0xffffffff
   0x00000000004007b4 <+94>:	add    eax,ecx
   0x00000000004007b6 <+96>:	mov    ecx,eax
   0x00000000004007b8 <+98>:	movsxd rax,edx
   0x00000000004007bb <+101>:	mov    BYTE PTR [rax+0x6010e0],cl
   0x00000000004007c1 <+107>:	add    DWORD PTR [rbp-0x40],0x1
   0x00000000004007c5 <+111>:	jmp    0x400775 <main+31>
   0x00000000004007c7 <+113>:	movabs rax,0x616c662f706d742f
   0x00000000004007d1 <+123>:	mov    QWORD PTR [rbp-0x30],rax
   0x00000000004007d5 <+127>:	mov    DWORD PTR [rbp-0x28],0x78742e67
   0x00000000004007dc <+134>:	mov    WORD PTR [rbp-0x24],0x74
   0x00000000004007e2 <+140>:	lea    rax,[rbp-0x30]
   0x00000000004007e6 <+144>:	mov    esi,0x400974
   0x00000000004007eb <+149>:	mov    rdi,rax
   0x00000000004007ee <+152>:	call   0x400650 <fopen@plt>
   0x00000000004007f3 <+157>:	mov    QWORD PTR [rbp-0x38],rax
   0x00000000004007f7 <+161>:	mov    rax,QWORD PTR [rbp-0x38]
   0x00000000004007fb <+165>:	mov    edx,0x601120
---Type <return> to continue, or q <return> to quit---
   0x0000000000400800 <+170>:	mov    esi,0x400976
   0x0000000000400805 <+175>:	mov    rdi,rax
   0x0000000000400808 <+178>:	mov    eax,0x0
   0x000000000040080d <+183>:	call   0x400620 <fprintf@plt>
   0x0000000000400812 <+188>:	mov    DWORD PTR [rbp-0x3c],0x0
   0x0000000000400819 <+195>:	mov    eax,DWORD PTR [rbp-0x3c]
   0x000000000040081c <+198>:	movsxd rbx,eax
   0x000000000040081f <+201>:	mov    edi,0x6010e0
   0x0000000000400824 <+206>:	call   0x4005e0 <strlen@plt>
   0x0000000000400829 <+211>:	cmp    rbx,rax
   0x000000000040082c <+214>:	jae    0x4008b5 <main+351>
   0x0000000000400832 <+220>:	mov    eax,DWORD PTR [rbp-0x3c]
   0x0000000000400835 <+223>:	cdqe
   0x0000000000400837 <+225>:	mov    eax,DWORD PTR [rax*4+0x601160]
   0x000000000040083e <+232>:	movsxd rcx,eax
   0x0000000000400841 <+235>:	mov    rax,QWORD PTR [rbp-0x38]
   0x0000000000400845 <+239>:	mov    edx,0x0
   0x000000000040084a <+244>:	mov    rsi,rcx
   0x000000000040084d <+247>:	mov    rdi,rax
   0x0000000000400850 <+250>:	call   0x400640 <fseek@plt>
   0x0000000000400855 <+255>:	mov    eax,DWORD PTR [rbp-0x3c]
   0x0000000000400858 <+258>:	cdqe
   0x000000000040085a <+260>:	mov    eax,DWORD PTR [rax*4+0x601160]
   0x0000000000400861 <+267>:	cdqe
   0x0000000000400863 <+269>:	movzx  eax,BYTE PTR [rax+0x6010e0]
   0x000000000040086a <+276>:	movsx  eax,al
   0x000000000040086d <+279>:	mov    rdx,QWORD PTR [rbp-0x38]
   0x0000000000400871 <+283>:	mov    rsi,rdx
   0x0000000000400874 <+286>:	mov    edi,eax
   0x0000000000400876 <+288>:	call   0x400600 <fputc@plt>
   0x000000000040087b <+293>:	mov    rax,QWORD PTR [rbp-0x38]
   0x000000000040087f <+297>:	mov    edx,0x0
   0x0000000000400884 <+302>:	mov    esi,0x0
   0x0000000000400889 <+307>:	mov    rdi,rax
   0x000000000040088c <+310>:	call   0x400640 <fseek@plt>
   0x0000000000400891 <+315>:	mov    rax,QWORD PTR [rbp-0x38]
   0x0000000000400895 <+319>:	mov    edx,0x601120
   0x000000000040089a <+324>:	mov    esi,0x400976
   0x000000000040089f <+329>:	mov    rdi,rax
   0x00000000004008a2 <+332>:	mov    eax,0x0
   0x00000000004008a7 <+337>:	call   0x400620 <fprintf@plt>
   0x00000000004008ac <+342>:	add    DWORD PTR [rbp-0x3c],0x1
   0x00000000004008b0 <+346>:	jmp    0x400819 <main+195>
   0x00000000004008b5 <+351>:	mov    rax,QWORD PTR [rbp-0x38]
   0x00000000004008b9 <+355>:	mov    rdi,rax
---Type <return> to continue, or q <return> to quit---
   0x00000000004008bc <+358>:	call   0x4005d0 <fclose@plt>
   0x00000000004008c1 <+363>:	lea    rax,[rbp-0x30]
   0x00000000004008c5 <+367>:	mov    rdi,rax
   0x00000000004008c8 <+370>:	call   0x4005c0 <remove@plt>
   0x00000000004008cd <+375>:	mov    eax,0x0
   0x00000000004008d2 <+380>:	mov    rbx,QWORD PTR [rbp-0x18]
   0x00000000004008d6 <+384>:	xor    rbx,QWORD PTR fs:0x28
   0x00000000004008df <+393>:	je     0x4008e6 <main+400>
   0x00000000004008e1 <+395>:	call   0x4005f0 <__stack_chk_fail@plt>
   0x00000000004008e6 <+400>:	add    rsp,0x38
   0x00000000004008ea <+404>:	pop    rbx
   0x00000000004008eb <+405>:	pop    rbp
   0x00000000004008ec <+406>:	ret
End of assembler dump.
(gdb)
```

Here we need to create a break point in:
```
0x00000000004008bc <+358>:	call   0x4005d0 <fclose@plt>
```

Let's create the break point and run
```
(gdb) break *0x00000000004008bc
Breakpoint 1 at 0x4008bc
(gdb) run
Starting program: /tmp/getit

Breakpoint 1, 0x00000000004008bc in main ()
(gdb)
```

Now we can check the output of the flag.txt into the tmp directory
```bash
 cat /tmp/flag.txt
*********{*********************************
```

Back in the output of ltrace we have a strlen call right after the fprintf
```bash
fopen("/tmp/flag.txt", "w")                                                                                                                                     = 0x8f8010
fprintf(0x8f8010, "%s\n", "********************************"...)                                                                                                = 44
strlen("SharifCTF{b70c59275fcfa8aebf2d59"...)                                                                                                                   = 43
```


So the output file does not have the correct flag value, so let's back to the gdb. Quite the current session and let's open another.
```bash
gdb -q
(gdb) file getit
Reading symbols from getit...(no debugging symbols found)...done.
(gdb) set disassembly-flavor intel
(gdb) disassemble main
[...]
   0x00000000004007ee <+152>:	call   0x400650 <fopen@plt>
   0x00000000004007f3 <+157>:	mov    QWORD PTR [rbp-0x38],rax
   0x00000000004007f7 <+161>:	mov    rax,QWORD PTR [rbp-0x38]
   0x00000000004007fb <+165>:	mov    edx,0x601120
---Type <return> to continue, or q <return> to quit---
   0x0000000000400800 <+170>:	mov    esi,0x400976
   0x0000000000400805 <+175>:	mov    rdi,rax
   0x0000000000400808 <+178>:	mov    eax,0x0
   0x000000000040080d <+183>:	call   0x400620 <fprintf@plt>
   0x0000000000400812 <+188>:	mov    DWORD PTR [rbp-0x3c],0x0
   0x0000000000400819 <+195>:	mov    eax,DWORD PTR [rbp-0x3c]
   0x000000000040081c <+198>:	movsxd rbx,eax
   0x000000000040081f <+201>:	mov    edi,0x6010e0
   0x0000000000400824 <+206>:	call   0x4005e0 <strlen@plt>
```

As we can see here we have the mov of edi right before the strlen call and we have the value of 0x6010e0 let's inspect this guy, let's create a break point in the strlen call and check the value of the 0x6010e0
```bash
(gdb) break *0x0000000000400824
Breakpoint 1 at 0x400824
(gdb) run
Starting program: /tmp/getit

Breakpoint 1, 0x0000000000400824 in main ()
```

Now let's check the value of 0x6010e0
```bash
(gdb) x/s 0x6010e0
0x6010e0 <t>:	"SharifCTF{b70c59275fcfa8aebf2d5911223c6589}"
```

The flag is: SharifCTF{b70c59275fcfa8aebf2d5911223c6589}
