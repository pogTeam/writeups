~~~
Perhaps this time I'll have hidden things a little better... you won't find my flag so easily now! nicebowlofsoup.com
HINT: How do slave zones know when updates are made to the master? 
~~~
    
First thing to notice here is that accessing `nicebowlofsoup.com` leads to a 404 error. According to the hint and the title, the solution pobably relies on `dig`and `zone transfers`.

Lets give it a first try.

~~~
$ dig nicebowlofsoup.com any

; <<>> DiG 9.10.3-P4-Debian <<>> nicebowlofsoup.com any
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 2135
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;nicebowlofsoup.com.INANY

;; Query time: 17           msec
;; SERVER: 2804:14c:6510:672:189:6:0:182#53(2804:14c:6510:672:189:6:0:182)
;; WHEN: Mon Feb 12 18:08:36 -02 2018
;; MSG SIZE  rcvd: 47
~~~

Nice, an IPv6 server address! So now we can query this server using `-6` option.

~~~
$ dig -6 @2804:14c:6510:672:189:6:0:182 nicebowlofsoup.com any

; <<>> DiG 9.10.3-P4-Debian <<>> -6 @2804:14c:6510:672:189:6:0:182 nicebowlofsoup.com any
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 6071
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 2, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;nicebowlofsoup.com.INANY

;; ANSWER SECTION:
nicebowlofsou           p.com.100INTXT"Close, but no cigar... where else could it be? hint:              the nameserver's IP is 159.65.43.62"
nicebowlofsoup.com.86400INSOA               ns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
nicebowlofsoup.com.170405INNSns2.nicebowlofsoup.c               om.
nicebowlofsoup.com.170405INNSns1.nicebowlofsoup.com.

;; AUTHOR               ITY SECTION:
nicebowlofsoup.com.170405INNSns2.nicebowlofsoup.com.
n               icebowlofsoup.com.170405INNSns1.nicebowlofsoup.com.

;; Query time:               148 msec
;; SERVER: 2804:14c:6510:672:189:6:0:182#53(2804:14c:6510:672:189:6:0:182)
;; WHEN: Mon Feb 12 17:54:55 -02 2018
;; MSG SIZE  rcvd: 259
~~~

Ok, now that we have the nameserver's IPv4 address, lets try the zone transfer.

~~~
$ dig @159.65.43.62 nicebowlofsoup.com axfr

; <<>> DiG 9.10.3-P4-Debian <<>> @159.65.43.62 nicebowlofsoup.com axfr
; (1 server found)
;; global options: +cmd
nicebowlofsoup.com.86400INSOAns1.nicebowlofsoup.com. hos                tmaster.nicebowlofsoup.com. 2018021205 28800 7200 604800 86400
easyctf.nicebowlofsoup.com. 10INTXT"easyctf{why_do_i_even_have_this_domain}"
nicebowlo           fsoup.com.100INTXT"Close, but no cigar... where else could it be? h             int: the nameserver's IP is 159.65.43.62"
nicebowlofsoup.com.86400IN          SOAns1.nicebowlofsoup.com. hostmaster.nicebowlofsoup.com. 2018021205 2  8800 7200 604800 86400
;; Query time: 438 msec
;; SERVER: 159.65.43.62#53(159.65.43.62)
;; WHEN: Mon Feb 12 18:03:28 -02 2018
;; XFR size: 4 records (messages 3, bytes 404)
~~~

:)
