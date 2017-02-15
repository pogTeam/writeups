# Fore1: Hit the core

## Description

No description!

## Solution

A simple strings command in the binary showed us an interesting string:

```
cvqAeqacLtqazEigwiXobxrCrtuiTzahfFreqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}
```

Our team mates cyborg, mvalle and nano, found the string ALEXCTF inside the scrambled text:


cvq<b>A</b>eqac<b>L</b>tqaz<b>E</b>igwi<b>X</b>obxr<b>C</b>rtui<b>T</b>zahf<b>F</b>reqc{bnjrKwgk83kgd43j85ePgb_e_rwqr7fvbmHjklo3tews_hmkogooyf0vbnk0ii87Drfgh_n kiwutfb0ghk9ro987k5tfb_hjiouo087ptfcv}

After a few minutes, cyborg got the rest of the string:

cvq<b>A</b>eqac<b>L</b>tqaz<b>E</b>igwi<b>X</b>obxr<b>C</b>rtui<b>T</b>zahf<b>F</b>reqc{bnjr<b>K</b>wgk8<b>3</b>kgd4<b>3</b>j85e<b>P</b>gb_e_rwqr<b>7</b>fvbm<b>H</b>jklo<b>3</b>tews_hmko<b>g</b>ooyf<b>0</b>vbnk<b>0</b>ii87<b>D</b>rfgh_n ki<b>w</b>utfb<b>0</b>ghk9ro987<b>k</b>5tfb_hjio<b>u</b>o087<b>p</b>tfcv}

Flag: ALEXCTF{K33P_7H3_g00D_w0rk_up}