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
chrome.get('https://demoqa.com/alerts')

# sleep time to see the action of testing
sleep(2)

# complete username  - attribute - value -
chrome.find_element(By.ID, 'alertButton').click()
sleep(2)

chrome.switch_to.alert.accept()
sleep(2)

# close Chrome
chrome.quit()

# it the test is ok we receive the msg
print('SUCCESS - TEST PASSED')
