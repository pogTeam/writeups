# Web1

## Description

Chris Martin wants to go home. Can you help him get there as soon as possible?


## Solution

Once I took to long to write this, the environment for Nullcon HackIM is not available anymore, so I'll just put the things I remember :D

When you enter the website, in the end of the source code there was a base64 string: <b>MmI0YjAzN2ZkMWYzMDM3NWU1Y2Q4NzE0NDhiNWI5NWM=</b> which decoded is a md5 hash <b>2b4b037fd1f30375e5cd871448b5b95c</b>.

![1](1.png)

After get these values, I tried to curl the flag but I was getting an error message.
I saw a hint in the Nullcon twitter: 'There's no place like home' and a friend that I made in the contest (thanks [@menztrual](https://twitter.com/menztrual) from TheGoonies ;)) cleared my mind:

curl -v --header "X-Forwarded-For: 127.0.0.1" --data "user=coldplay&pass=paradise" -X POST "http://54.152.19.210/web100/"

The header <b>X-Forwarded-For</b> was the catch!

Flag: flag{4f9361b0302d4c2f2eb1fc308587dfd6}