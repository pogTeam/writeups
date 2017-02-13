# Programmin question 1 - 200pts

~~~~
We unearthed this text file from one of the older servers and want to know what this is all about. Could you please analyse this and let us know your finding?

abc.txt
~~~~

## Solution

The file gives us a list of triplets which obviously seem like pixels, since most of them are (255, 255, 255), i.e., black pixel. The standard python module for image manipulation is *PIL* so all we had to do was reading the pixels and creating an image from it.

In order to read the list as a list and not a string, we trusted eval() (!DANGER!). Fortnuately HackIM guys did not insert a malware in the middle of that mess :)

The second point we had to think about was image dimensions. Ok, here are the pixels, but how should we display then? 512x512? 1000x1000? First I realized (!) the product of the dimensions must be the quantity of tuples (yep, the area of a square). The solution is pretty obvious actually, although it took me almost an hour to figure it out. My first idea was to brute force the dimensions: factorize the lenght of the list into primes and try all possible integers *a* and *b* such that *a*b = len(list)\*.

It happens I was complicating it. The lenght of the list is 528601, which, according to factorDB, is 569\*929. So there you go, with the dimensions the solution is straight forward.

