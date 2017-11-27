# Cookie Harrelson (200pts)

## Description

~~~
Woody Harrelson has decided to take up web dev after learning about Cookies. Show him that he should go back to killing zombies.

Note: index.txt is what is being displayed on the page.

http://cookieharrelson.tuctf.com
~~~

## Solution

We start by looking at the cookies with CookieMonster extension. In the cookie `tallahassee` there is a URL encoded, base64 encoded text:

    cat index.txt

We first tried editing this cookie to `cat flag` or `cat flag.txt`. After refreshing the page, we checked the cookie and found:

    cat index.txt #cat flag

So our command is probably being commented in a Shell Script way. After a lot of thinking and some friends helping, we found the solution with multi line commands:

    \
    cat flag

After refreshing:

    cat index #\
    cat flag

The flag shows up in the page:

    TUCTF{D0nt_3x3cut3_Fr0m_c00k13s}

Again, don't!
