# Git Gud (100pts)

## Description

    Jimmy has begun learning about Version Control Systems and decided it was a good time to put it into use for his person website. Show him how to Git Gud.
    
    http://gitgud.tuctf.com

## Solution

The challenge gives a URL with apparently nothing useful. Due to the tile we thought about a git repo somewhere in this domain. We found it manually at:

    http://http://gitgud.tuctf.com/.git

The biggest difficulty was to download the repo, sice `git clone` did not work. So we downloaded it recursively with:

    $ wget -r http://gitgud.tuctf.com/.git

In the `.git/log` folder we could see that the flag was added with commit `4fa0acbccd0885dace2f111f2bd7a120abc0fb4e`:

However, before checking out into this commit, we needed to stash the changes:

    $ git stash

Now we were able to:

    $ git checkout 4fa0acbccd0885dace2f111f2bd7a120abc0fb4
    HEAD is now at 4fa0acb... Added flag

Finally:

~~~
$ git show
commit 4fa0acbccd0885dace2f111f2bd7a120abc0fb4e
Author: Jimmy <jimmy@jimmyrocks.site>
Date:   Tue Nov 21 20:47:00 2017 +0000

    Added flag

    diff --git a/flag b/flag
    new file mode 100644
    index 0000000..1b8dce4
    --- /dev/null
    +++ b/flag
    @@ -0,0 +1,2 @@
    +
    +TUCTF{D0nt_M4k3_G1t_Publ1c}
~~~

So, yeah, just don't do it :)
