#Hot Sun?

~~~~
[EN] 
Surfing in the Shallowweb, we have discovered a new algorithm that promises to be the newest substituition cipher. The algorithm to encrypt works as following: the user informs the text to be encrypted and a number N. Initially, the algorithm shift all letters one position to the right (e.g. 'A' tuns into 'B'). With this result, in the next step, the algorithm now shift the text two positions to the right. And with the text from the previous output, it repeats the shift procedure until N. Your task is quite simple: given an encrypted flag and an N number, discover the flag. 
Encrypted flag: 3RG{hv1g_f0h_1g_b0h_g0_V0h} N: 11 

[PT-BR]
Pesquisando na shallowweb, descobrimos um novo algoritmo que promete ser a mais nova cifra de substituicao. O algoritmo para cifrar funciona da seguinte forma: o usuraio informa o texto a ser cifrado e um numero N. O algoritmo, inicialmente, desloca todas as letras em uma posicao a direita ('A', por exemplo, vira 'B). Com o texto da saida, no passo seguinte, o algoritmo desloca esse novo texto duas posicoes a direita. E com o texto da saida anterior, ele repete o procedimento de deslocamentos ate o numero N. Sua tarefa bem simples: dado a flag cifrada e um numero N, descubra a flag. 
Flag cifrada: 3RG{hv1g_f0h_1g_b0h_g0_V0h} 
N: 11
~~~~

This is a very simple chall about ROTs. There are 2 approaches here: whether you try to really understand what is going on, ROT by ROT, or you just solve it.

We assumed a pretty obvious principle: the composition of ROTs is just another ROT. This means if you rotate *x* times to the right, then *y* to the left, then right again and so on, all this is equivlent to a single *ROT Z*. A nice example of an isomorphism.

Since the beginning of the flag must be *3DS*, we know that *R* goes to *D*. This means that we are rotating everything *ord ('R') - ord('D') == 14*. A simple ROT14 then. The flag should be 3DS{th1s_r0t_1s_n0t_s0_H0t}.
