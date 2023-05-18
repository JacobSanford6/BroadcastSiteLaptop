import requests
import time
from selenium import webdriver



lastRaw=  None
url = "http://jacobsanford.ddns.net:5000"

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.implicitly_wait(0.5)

driver.get(url)

# Refreshes display
def refreshPage():
    global driver
    driver.refresh()

# Check if website has changed every half second
# If website has changed, refresh the page
while True:
    time.sleep(.5)
    rq = requests.get(url)
    if lastRaw != rq.text:
        refreshPage()
    lastRaw = rq.text
    rq.close()
    
