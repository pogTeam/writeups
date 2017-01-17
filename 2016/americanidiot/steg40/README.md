### steg40

O arquivo baixado � uma imagem do pent�gono, apenas isso. Em um primeiro momento achei que existia alguma informa��o nos *metadados* da imagem.

Iniciei verificando com os metadados ta imagem com o utilit�rio exiftool[1]:

```bash
[rafael@localhost steg40]$ sudo dnf search exiftool
perl-Image-ExifTool.noarch : Utility for reading and writing image meta info
[rafael@localhost steg40]$ exiftool pentagono.jpg
```
Sem nenhum retorno, iniciei a pesquisa por maneiras de inserir arquivos dentro de outros arquivos at� encontrar o utilit�rio steghide[2].

```bash
[rafael@localhost steg40]$ dnf search steghide
steghide.x86_64 : A steganography program
[rafael@localhost steg40]$ steghide extract -sf pentagono.jpg
Enter passphrase:
```

A grande sacada � que para extrair os arquivos, � necess�rio uma senha.
Depois de muito tempo sem entender o enunciando, percebi que existia uma informa��o que deixei passar em branco:

> SIGLA: 38.9486982, -77.4565925

As coordenadas acima apontam para o *Aeroporto Internacional Washington Dulles* cuja sigla � IAD. Com essa informa��o, a flag foi conquistada:

```bash
[rafael@localhost steg40]$ steghide extract -sf pentagono.jpg
Enter passphrase: #IAD
wrote extracted data to ".flag.txt".
[rafael@localhost steg40]$ cat .flag.txt
SHC{PlanOfTheBuilding}
```

Links:

[[1] - Exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/)

[[2] - Steghide](http://steghide.sourceforge.net/)
