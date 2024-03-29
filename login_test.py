# import selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initialize Chrome
chrome = webdriver.Chrome()

# max window
chrome.maximize_window()

# navigate to a link
chrome.get('https://the-internet.herokuapp.com/login')

# sleep time to see the action of testing
sleep(2)

# complete username  - attribute - value -
chrome.find_element(By.XPATH, '//input[@name="username"]').send_keys('tomsmith')
sleep(2)

chrome.find_element(By.XPATH, '//*[@id="password"]').send_keys('SuperSecretPassword!')
sleep(2)

# click link  -- text element --
chrome.find_element(By.XPATH, '//*[text()=" Login"]').click()
sleep(2)

# check login page pass ok
expected = 'https://the-internet.herokuapp.com/secure'
actual = chrome.current_url
assert expected == actual, 'incorrect url'


# close Chrome
chrome.quit()

# it the test is ok we receive the msg
print('SUCCESS - TEST PASSED')
