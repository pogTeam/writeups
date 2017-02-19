# Web2

## Description

There are two kinds of people in this world. One with all the privileges and the others. Can you get the flag by eating some British biscuit?


## Solution

As the same in Web1: Once I took to long to write this, the environment for Nullcon HackIM is not available anymore, so I'll just put the things I remember :D

The site requires a user and password, and it gives us an interface to register it by ourselves.
In the challenge description the admin mentioned something about cookies, so, here's the logic behind it.
By the time you log in to the system, it creates two cookies, r and u and there was a constant part in both <b>351e766803</b>.

```php
User: pog - Password: pog

cookie: r = 351e766803 + d63c7ede8cb1e1c8db5e51c63fd47cff (limited)
cookie: u = 351e766803 + 5bb50314c7d970ce6cb07afb583c4c9d (pog)
```

Removing this, the other part is a md5 hash from the user access and the username, respectively. So, following this approach, I tried to generate a md5 hash for unlimited, administrator and the ones which worked, was <b>admin</b>! :D

Flag: flag{1e39bd297a47ed0eeaea9cac7e}