import requests
import time
from selenium import webdriver



lastRaw=  None
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)

driver.get("http://jacobsanford.ddns.net:5000")

def refreshPage():
    global driver
    driver.refresh()

while True:
    time.sleep(.5)
    rq = requests.get("http://167.248.46.73:5000")
    if lastRaw != rq.text:
        refreshPage()
    lastRaw = rq.text
    rq.close()
    
