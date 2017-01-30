from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome('/opt/_CTF/breakin/chromedriver')
chrome.get('https://felicity.iiit.ac.in/contest/extra/fastandfurious')

while(True):
    # Get operands
    operation = chrome.find_element_by_xpath('/html/body/p[2]')
    op = operation.text[6:].strip()
    # Execute operation
    ans = eval(op)
    
    # Write answer into the box 
    ques_ans = chrome.find_element_by_name('ques_ans')
    ques_ans.send_keys(ans)

    # Presse enter
    ques_ans.send_keys(Keys.ENTER)

