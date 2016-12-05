from urllib.request import urlopen
import re

url = "https://ctf.sucurihc.org/flag/oldreligion/web20/index.html"

print("[DEBUG] >> Opening url {}".format(url))
conteudo = urlopen(url).read().decode("ISO-8859-1")

print("[DEBUG] <<< Viewing content {}".format(conteudo))
resultado = re.findall("alt=\"(.*?)(\"/|\" /)>", conteudo)

flag = ""
for letras in resultado:
    #print(str(letras[0]))
    flag += letras[0]

print("Flag: {}".format(flag))