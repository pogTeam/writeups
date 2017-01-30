We were given a silly web page with an arithmetic operation and a submit box. However, we should answer it *Fast and Furious*, so no time to manually do the math. 

I first tried using python *requests* but I changed my mind when I realized I would need one request to get the operation and then another to answer it. But by the time I sent the response to the first request, the operation would have changed. I needed something more interactive, like a Javascript code.

Fortunately I had heard of [Selenium project](http://www.seleniumhq.org/docs/01_introducing_selenium.jsp) a tool for web browser automation, normally used for testing purposes. Therefore I moved on to Selenium webdriver, so I could use it within my python script (I really enjoy Python. Like, REALLY). This was a cool experience, since I wanted to try this tool for a long time. The results are amazing, it allows us to interact with the browser just as if we were pointing and clicking it. This should do the trick for now.

After running

    pip install selenium , 

I got some errors since it was not finding the browser drivers (chrome driver in this case). Instead of exporting the dirver path to PATH env variable, I chose to download the package manually and hardcode it.

In order to get the operands I used an XPath query. Although it is a very simple query, I used *Firebug's* "copy xpath" feature (just click with the right button over the desired element and click the xpath option).

The eval() function (**!!DANGER!!**) was very useful too to evaluate a math expression from the retrieved string.

After simulating the 'enter' key, it started running. Like really running, a browser was opened and things started happening there, as if I was clicking stuff myself. I got inebriated, no black screen, no green charachters. So futuristic. After about 200 levels we got the answer.

    the_flag_is_6ffb242e3f65a2b51c36745b1cd591d1
