from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyfiglet
ident = "Message Spammer!"
asciia = pyfiglet.figlet_format(ident)
num = 1
print(asciia)
print("By zyog4uss")
print("starting Spammer...")
cnum = 6
for i in range(5):
    time.sleep(1)
    cnum = cnum - 1
    print(cnum)
print("Spammer ready!")
    
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

while True:
    driver.get("https://www.stjohns.excalibur.org.uk")
    time.sleep(10)
    email_input = driver.find_element(By.XPATH, '//*[@id="nf-field-2"]')
    email_input.send_keys("zyogauss@gmail.com")
    message_input = driver.find_element(By.XPATH, '//*[@id="nf-field-3"]')
    message_input.send_keys("zyog4uss has spammed you using a script I wrote!! this is the ", num, " st/nd", " time this has happened")
    num = num + 1
    email_input.send_keys(Keys.ENTER)
    time.sleep(3)
    



