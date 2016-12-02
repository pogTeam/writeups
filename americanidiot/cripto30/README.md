### critpo30

O arquivo baixado � um �udio .wav do presidente dos EUA Barack Obama anunciando a morte de Osama Bin Laden. Aparentemente n�o h� nada de errado com o arquivo, mas com um pouco de paci�ncia chegamos aos �ltimos segundos do �udio, em que se ouve um ru�do, como se a flag falasse conosco :)

Abrindo com o Audacity, podemos ver claramente o ru�do a partir do tempo 1:15, mas n�o parece dizer muito. 

![Ruido](audio1.png)

Como o chall falava de duas t�cnicas, incluindo uma de cripto, pensei que o ru�do poderia ser um c�digo morse, bin�rio, ou qualquer coisa do tipo. Como n�o achei nada disso, parti para outras an�lises da onda.

O Audacity permite que visualizemos o �udio pelo espectrograma, ao inv�s do formato da onda. Para isso basta selecionar a op��o na seta � esquerda da onda (audio).

![Flag](flag.png)

Agora sim! Claramente nossa flag criptografada. Pelo formato � bem prov�vel que seja uma cifra de substitui��o bem simples, como c�sar. Testando online (aqui)[http://www.xarg.org/tools/caesar-cipher/) vemos que realmente � de fato um ROT23.

O �nico problema � que essa flag n�o � aceita! Talvez o challenger quisesse colocar um pouco de guessing ou foi um erro de digita��o mesmo. Adicionando o *e* que falta fechamos a quest�o :)

    flag: SHC{AudioInterceptMensagem}
