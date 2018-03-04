
# Assemble your way to the flag (50 pts)

~~~
My friend was trying out assembly for the first time, he has no clue what he's doing, help him out and procure your reward in the form of a flag :)
~~~

~~~
$ gdb -q ./question 
Reading symbols from ./question...(no debugging symbols found)...done.
gdb-peda$ run
Starting program: /home/valle/Downloads/question 
Look for something else....
[Inferior 1 (process 1612) exited normally]
Warning: not running or target is remote
gdb-peda$ pdisass main
Dump of assembler code for function main:
   0x00005555555546a0 <+0>:	push   rbp
   0x00005555555546a1 <+1>:	mov    rbp,rsp
   0x00005555555546a4 <+4>:	lea    rdi,[rip+0x2b9]        # 0x555555554964
   0x00005555555546ab <+11>:	mov    eax,0x0
   0x00005555555546b0 <+16>:	mov    rax,0x50
   0x00005555555546b7 <+23>:	mov    rbx,0x2d
   0x00005555555546be <+30>:	xor    rax,rbx
   0x00005555555546c1 <+33>:	push   rax
   0x00005555555546c2 <+34>:	mov    rax,0xc1
   0x00005555555546c9 <+41>:	mov    rbx,0xb8
   0x00005555555546d0 <+48>:	xor    rax,rbx
   0x00005555555546d3 <+51>:	push   rax
   0x00005555555546d4 <+52>:	mov    rax,0x51
   0x00005555555546db <+59>:	mov    rbx,0x60
   0x00005555555546e2 <+66>:	xor    rax,rbx
   0x00005555555546e5 <+69>:	push   rax
   0x00005555555546e6 <+70>:	mov    rax,0x33
   0x00005555555546ed <+77>:	mov    rbx,0x51
   0x00005555555546f4 <+84>:	xor    rax,rbx
   0x00005555555546f7 <+87>:	push   rax
   0x00005555555546f8 <+88>:	mov    rax,0x45
   0x00005555555546ff <+95>:	mov    rbx,0x28
   0x0000555555554706 <+102>:	xor    rax,rbx
   0x0000555555554709 <+105>:	push   rax
   0x000055555555470a <+106>:	mov    rax,0x9b
   0x0000555555554711 <+113>:	mov    rbx,0xa8
   0x0000555555554718 <+120>:	xor    rax,rbx
   0x000055555555471b <+123>:	push   rax
   0x000055555555471c <+124>:	mov    rax,0x71
   0x0000555555554723 <+131>:	mov    rbx,0x2
   0x000055555555472a <+138>:	xor    rax,rbx
   0x000055555555472d <+141>:	push   rax
   0x000055555555472e <+142>:	mov    rax,0x8b
   0x0000555555554735 <+149>:	mov    rbx,0xd8
   0x000055555555473c <+156>:	xor    rax,rbx
   0x000055555555473f <+159>:	push   rax
   0x0000555555554740 <+160>:	mov    rax,0x98
   0x0000555555554747 <+167>:	mov    rbx,0xac
   0x000055555555474e <+174>:	xor    rax,rbx
   0x0000555555554751 <+177>:	push   rax
   0x0000555555554752 <+178>:	mov    rax,0x8e
   0x0000555555554759 <+185>:	mov    rbx,0xd1
   0x0000555555554760 <+192>:	xor    rax,rbx
   0x0000555555554763 <+195>:	push   rax
   0x0000555555554764 <+196>:	mov    rax,0x66
   0x000055555555476b <+203>:	mov    rbx,0x8
   0x0000555555554772 <+210>:	xor    rax,rbx
   0x0000555555554775 <+213>:	push   rax
   0x0000555555554776 <+214>:	mov    rax,0xa9
   0x000055555555477d <+221>:	mov    rbx,0x98
   0x0000555555554784 <+228>:	xor    rax,rbx
   0x0000555555554787 <+231>:	push   rax
   0x0000555555554788 <+232>:	mov    rax,0x65
   0x000055555555478f <+239>:	mov    rbx,0x3a
   0x0000555555554796 <+246>:	xor    rax,rbx
   0x0000555555554799 <+249>:	push   rax
   0x000055555555479a <+250>:	mov    rax,0x7e
   0x00005555555547a1 <+257>:	mov    rbx,0x4d
   0x00005555555547a8 <+264>:	xor    rax,rbx
   0x00005555555547ab <+267>:	push   rax
   0x00005555555547ac <+268>:	mov    rax,0x10
   0x00005555555547b3 <+275>:	mov    rbx,0x74
   0x00005555555547ba <+282>:	xor    rax,rbx
   0x00005555555547bd <+285>:	push   rax
   0x00005555555547be <+286>:	mov    rax,0x6b
   0x00005555555547c5 <+293>:	mov    rbx,0x5b
   0x00005555555547cc <+300>:	xor    rax,rbx
   0x00005555555547cf <+303>:	push   rax
   0x00005555555547d0 <+304>:	mov    rax,0x98
   0x00005555555547d7 <+311>:	mov    rbx,0xfb
   0x00005555555547de <+318>:	xor    rax,rbx
   0x00005555555547e1 <+321>:	push   rax
   0x00005555555547e2 <+322>:	mov    rax,0xc5
   0x00005555555547e9 <+329>:	mov    rbx,0x9a
   0x00005555555547f0 <+336>:	xor    rax,rbx
   0x00005555555547f3 <+339>:	push   rax
   0x00005555555547f4 <+340>:	mov    rax,0x37
   0x00005555555547fb <+347>:	mov    rbx,0x44
   0x0000555555554802 <+354>:	xor    rax,rbx
   0x0000555555554805 <+357>:	push   rax
   0x0000555555554806 <+358>:	mov    rax,0x92
   0x000055555555480d <+365>:	mov    rbx,0xf6
   0x0000555555554814 <+372>:	xor    rax,rbx
   0x0000555555554817 <+375>:	push   rax
   0x0000555555554818 <+376>:	mov    rax,0x44
   0x000055555555481f <+383>:	mov    rbx,0xa
   0x0000555555554826 <+390>:	xor    rax,rbx
   0x0000555555554829 <+393>:	push   rax
   0x000055555555482a <+394>:	mov    rax,0x80
   0x0000555555554831 <+401>:	mov    rbx,0xe5
   0x0000555555554838 <+408>:	xor    rax,rbx
   0x000055555555483b <+411>:	push   rax
   0x000055555555483c <+412>:	mov    rax,0xc8
   0x0000555555554843 <+419>:	mov    rbx,0xaf
   0x000055555555484a <+426>:	xor    rax,rbx
   0x000055555555484d <+429>:	push   rax
   0x000055555555484e <+430>:	mov    rax,0x26
   0x0000555555554855 <+437>:	mov    rbx,0x15
   0x000055555555485c <+444>:	xor    rax,rbx
   0x000055555555485f <+447>:	push   rax
   0x0000555555554860 <+448>:	mov    rax,0x3e
   0x0000555555554867 <+455>:	mov    rbx,0x52
   0x000055555555486e <+462>:	xor    rax,rbx
   0x0000555555554871 <+465>:	push   rax
   0x0000555555554872 <+466>:	mov    rax,0x9a
   0x0000555555554879 <+473>:	mov    rbx,0xe1
   0x0000555555554880 <+480>:	xor    rax,rbx
   0x0000555555554883 <+483>:	push   rax
   0x0000555555554884 <+484>:	mov    rax,0x13
   0x000055555555488b <+491>:	mov    rbx,0x75
   0x0000555555554892 <+498>:	xor    rax,rbx
   0x0000555555554895 <+501>:	push   rax
   0x0000555555554896 <+502>:	mov    rax,0xa2
   0x000055555555489d <+509>:	mov    rbx,0xd6
   0x00005555555548a4 <+516>:	xor    rax,rbx
   0x00005555555548a7 <+519>:	push   rax
   0x00005555555548a8 <+520>:	mov    rax,0xbe
   0x00005555555548af <+527>:	mov    rbx,0xdd
   0x00005555555548b6 <+534>:	xor    rax,rbx
   0x00005555555548b9 <+537>:	push   rax
   0x00005555555548ba <+538>:	mov    rax,0xac
   0x00005555555548c1 <+545>:	mov    rbx,0xdc
   0x00005555555548c8 <+552>:	xor    rax,rbx
   0x00005555555548cb <+555>:	push   rax
   0x00005555555548cc <+556>:	call   0x555555554560
   0x00005555555548d1 <+561>:	mov    eax,0x0
   0x00005555555548d6 <+566>:	add    rsp,0xf0
   0x00005555555548dd <+573>:	pop    rbp
   0x00005555555548de <+574>:	ret    
End of assembler dump.
gdb-peda$ break main
Breakpoint 1 at 0x5555555546a4
gdb-peda$ break *0x00005555555548d1
Breakpoint 2 at 0x5555555548d1
gdb-peda$ run
Starting program: /home/valle/Downloads/question 

[----------------------------------registers-----------------------------------]
RAX: 0x5555555546a0 (<main>:	push   rbp)
RBX: 0x0 
RCX: 0x0 
RDX: 0x7fffffffe168 --> 0x7fffffffe47a ("LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc"...)
RSI: 0x7fffffffe158 --> 0x7fffffffe45b ("/home/valle/Downloads/question")
RDI: 0x1 
RBP: 0x7fffffffe070 --> 0x5555555548e0 (<__libc_csu_init>:	push   r15)
RSP: 0x7fffffffe070 --> 0x5555555548e0 (<__libc_csu_init>:	push   r15)
RIP: 0x5555555546a4 (<main+4>:	lea    rdi,[rip+0x2b9]        # 0x555555554964)
R8 : 0x555555554950 (<__libc_csu_fini>:	repz ret)
R9 : 0x7ffff7de8cb0 (<_dl_fini>:	push   rbp)
R10: 0x4 
R11: 0x1 
R12: 0x555555554570 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe150 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x55555555469b <frame_dummy+43>:	jmp    0x5555555545e0 <register_tm_clones>
   0x5555555546a0 <main>:	push   rbp
   0x5555555546a1 <main+1>:	mov    rbp,rsp
=> 0x5555555546a4 <main+4>:	lea    rdi,[rip+0x2b9]        # 0x555555554964
   0x5555555546ab <main+11>:	mov    eax,0x0
   0x5555555546b0 <main+16>:	mov    rax,0x50
   0x5555555546b7 <main+23>:	mov    rbx,0x2d
   0x5555555546be <main+30>:	xor    rax,rbx
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffe070 --> 0x5555555548e0 (<__libc_csu_init>:	push   r15)
0008| 0x7fffffffe078 --> 0x7ffff7a5a2b1 (<__libc_start_main+241>:	mov    edi,eax)
0016| 0x7fffffffe080 --> 0x40000 
0024| 0x7fffffffe088 --> 0x7fffffffe158 --> 0x7fffffffe45b ("/home/valle/Downloads/question")
0032| 0x7fffffffe090 --> 0x1f7b9b2e8 
0040| 0x7fffffffe098 --> 0x5555555546a0 (<main>:	push   rbp)
0048| 0x7fffffffe0a0 --> 0x0 
0056| 0x7fffffffe0a8 --> 0x9ad5913901955e19 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x00005555555546a4 in main ()
gdb-peda$ c
Continuing.
Look for something else....









[----------------------------------registers-----------------------------------]
RAX: 0x1c 
RBX: 0xdc 
RCX: 0x7ffff7b15760 (<__write_nocancel+7>:	cmp    rax,0xfffffffffffff001)
RDX: 0x7ffff7dd5760 --> 0x0 
RSI: 0x555555756010 ("Look for something else....\n")
RDI: 0x555555756010 ("Look for something else....\n")
RBP: 0x7fffffffe070 --> 0x5555555548e0 (<__libc_csu_init>:	push   r15)
RSP: 0x7fffffffdf80 --> 0x70 ('p')
RIP: 0x5555555548d1 (<main+561>:	mov    eax,0x0)
R8 : 0x555555756000 --> 0x0 
R9 : 0x1c 
R10: 0x7ffff7dd3b58 --> 0x555555756410 --> 0x0 
R11: 0x246 
R12: 0x555555554570 (<_start>:	xor    ebp,ebp)
R13: 0x7fffffffe150 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5555555548c8 <main+552>:	xor    rax,rbx
   0x5555555548cb <main+555>:	push   rax
   0x5555555548cc <main+556>:	call   0x555555554560
=> 0x5555555548d1 <main+561>:	mov    eax,0x0
   0x5555555548d6 <main+566>:	add    rsp,0xf0
   0x5555555548dd <main+573>:	pop    rbp
   0x5555555548de <main+574>:	ret    
   0x5555555548df:	nop
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdf80 --> 0x70 ('p')
0008| 0x7fffffffdf88 --> 0x63 ('c')
0016| 0x7fffffffdf90 --> 0x74 ('t')
0024| 0x7fffffffdf98 --> 0x66 ('f')
0032| 0x7fffffffdfa0 --> 0x7b ('{')
0040| 0x7fffffffdfa8 --> 0x6c ('l')
0048| 0x7fffffffdfb0 --> 0x33 ('3')
0056| 0x7fffffffdfb8 --> 0x67 ('g')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x00005555555548d1 in main ()

0x7fffffffdff0:	0x00000030	0x00000000
gdb-peda$ x/30ws 0x7fffffffdf80
0x7fffffffdf80:	U"p"
0x7fffffffdf88:	U"c"
0x7fffffffdf90:	U"t"
0x7fffffffdf98:	U"f"
0x7fffffffdfa0:	U"{"
0x7fffffffdfa8:	U"l"
0x7fffffffdfb0:	U"3"
0x7fffffffdfb8:	U"g"
0x7fffffffdfc0:	U"e"
0x7fffffffdfc8:	U"N"
0x7fffffffdfd0:	U"d"
0x7fffffffdfd8:	U"s"
0x7fffffffdfe0:	U"_"
0x7fffffffdfe8:	U"c"
0x7fffffffdff0:	U"0"
0x7fffffffdff8:	U"d"
0x7fffffffe000:	U"3"
0x7fffffffe008:	U"_"
0x7fffffffe010:	U"1"
0x7fffffffe018:	U"n"
0x7fffffffe020:	U"_"
0x7fffffffe028:	U"4"
0x7fffffffe030:	U"S"
0x7fffffffe038:	U"s"
0x7fffffffe040:	U"3"
0x7fffffffe048:	U"m"
0x7fffffffe050:	U"b"
0x7fffffffe058:	U"1"
0x7fffffffe060:	U"y"
0x7fffffffe068:	U"}"
~~~
