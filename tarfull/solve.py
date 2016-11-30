# This solution uses recursion and IS NOT optimized. For better results, go for dynammic programming and use memoization. Or even better, just do the iterative stuff.
# You will probably need to increase ulimit (as root):
#   ulimit -u 2048
import zipfile
import tarfile
import magic
import os
import sys

def checkType( local ):
    if os.path.isdir(local):
        return "dir"
    else:
        return magic.from_file(local, mime=True) # gets file extension by oracle (solves files without explicit extension)

def extrai( local ):
    tipo = checkType(local)
    if "text" in tipo:
        with open(local) as f:
            print(f.readlines())
        return
    elif tipo=="dir":
        return
    elif "gzip" in tipo or "bzip2" in tipo:
        z = tarfile.open(local)
        nameList = z.getnames()
    elif "zip" in tipo:
        f = open(local, "rb")
        z = zipfile.ZipFile(f)
        nameList = z.namelist()

    z.close()

    for name in nameList:
        if tipo == "dir":
            continue
        elif name == "solve.py/": # dirty workaround for when the extracted file has the same name of the script
            os.rename("solve.py", "bananas.py")
            f = open(local, "rb")
            z = zipfile.ZipFile(f)
            z.extract(name, "")
            z.close()
            extrai(name)
        elif "gzip" in tipo or "bzip2" in tipo:
            print("[DEBUG >>>] New tar file: " + name)
            z = tarfile.open(local)
            z.extract(name, "")
            z.close()
            extrai(name)
        elif "zip" in tipo:
            print("[DEBUG >>>] New zip file: " + name)
            z = tarfile.open(local)
            z.extract(name, "")
            z.close()
            extrai(name)

### ATTENTION: RADIOACTIVE CODE! USE WITH CAUTION ###
sys.setrecursionlimit(3000) # dirty workaround for recursion depth limit
print("[DEBUG >>>] Function zip")
extrai("arq.zip")

# let's put things back in place :)
os.rename("solve.py/", "rep.py")
os.rename("bananas.py", "solve.py")
