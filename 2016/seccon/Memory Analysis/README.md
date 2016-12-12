# Memory Analysis
100 points
Memory Analysis
Find the website that the fake svchost is accessing.
You can get the flag if you access the website!!

memoryanalysis.zip

The challenge files are huge, please download it first.
Hint1: http://www.volatilityfoundation.org/
Hint2: Check the hosts file

## Resolution

After unzip the file memoryanalysis.zip we get the forensic_100.raw, as the tip was give we need to use the volatility to get it up.

Let's check the kind of the OS
```bash
vol.py -f forensic_100.raw imageinfo
Volatility Foundation Volatility Framework 2.5
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/Users/cyborg/Downloads/forensic_100.raw)
                      PAE type : PAE
                           DTB : 0x34c000L
                          KDBG : 0x80545ce0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2016-12-06 05:28:47 UTC+0000
     Image local date and time : 2016-12-06 14:28:47 +0900
```

Now we need to check if the hosts file exists
```bash
vol.py -f forensic_100.raw --profile=WinXPSP2x86 filescan | grep -i host
Volatility Foundation Volatility Framework 2.5
0x000000000201ef90      1      0 R--rw- \Device\HarddiskVolume1\WINDOWS\system32\svchost.exe
0x00000000020f0268      1      0 R--r-d \Device\HarddiskVolume1\WINDOWS\svchost.exe
0x000000000217b748      1      0 R--rw- \Device\HarddiskVolume1\WINDOWS\system32\drivers\etc\hosts
0x00000000024a7a90      1      0 R--rwd \Device\HarddiskVolume1\WINDOWS\system32\svchost.exe
```

Yep the file exists, let's extract it, so let's create a directory to store the file.
```bash
mkdir output
```

Now let's extract the file
```bash
vol.py -f forensic_100.raw --profile=WinXPSP2x86 dumpfiles -D output -Q 0x000000000217b748
Volatility Foundation Volatility Framework 2.5
DataSectionObject 0x0217b748   None   \Device\HarddiskVolume1\WINDOWS\system32\drivers\etc\hosts
```

Let's check the hosts file
```bash
cat output/file.None.0x819a3008.dat
# Copyright (c) 1993-1999 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

127.0.0.1       localhost
153.127.200.178    crattack.tistory.com
```

So the crattack.tistory.com does not work in the 153.127.200.178 ip address, let's check the correct one
```bash
nslookup crattack.tistory.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	crattack.tistory.com
Address: 175.126.170.110
Name:	crattack.tistory.com
Address: 175.126.170.70
```

Now let's check the iehistory
```bash
vol.py -f forensic_100.raw --profile=WinXPSP2x86 iehistory | grep -i "crattack.tistory.com"
Volatility Foundation Volatility Framework 2.5
Location: http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: Visited: SYSTEM@http://crattack.tistory.com/rss
Location: Visited: SYSTEM@http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: Visited: SYSTEM@http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: Visited: SYSTEM@http://crattack.tistory.com/rss
Location: Visited: SYSTEM@http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: Visited: SYSTEM@http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: :2016120620161207: SYSTEM@http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
Location: :2016120620161207: SYSTEM@:Host: crattack.tistory.com
Location: :2016120620161207: SYSTEM@http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd
```

As we can see the SYSTEM called sometimes http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd so let's check it up
```bash
curl -v 153.127.200.178/entry/Data-Science-import-pandas-as-pd
*   Trying 153.127.200.178...
* Connected to 153.127.200.178 (153.127.200.178) port 80 (#0)
> GET /entry/Data-Science-import-pandas-as-pd HTTP/1.1
> Host: 153.127.200.178
> User-Agent: curl/7.49.1
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: nginx/1.10.0 (Ubuntu)
< Date: Mon, 12 Dec 2016 11:43:10 GMT
< Content-Type: application/octet-stream
< Content-Length: 36
< Last-Modified: Tue, 06 Dec 2016 07:11:29 GMT
< Connection: keep-alive
< ETag: "584664a1-24"
< Accept-Ranges: bytes
<
SECCON{_h3110_w3_h4ve_fun_w4rg4m3_}
* Connection #0 to host 153.127.200.178 left intact
```

The flag is SECCON{_h3110_w3_h4ve_fun_w4rg4m3_}

## Links
- http://www.volatilityfoundation.org/
