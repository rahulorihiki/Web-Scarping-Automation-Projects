from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://web.whatsapp.com/")

data = input("Please Scan your QR code and then enter the message that you want to send")

# user = driver.find_element("title" , "Mahima Verma")
user = driver.find_element(By.CSS_SELECTOR, 'span[title="Mahima Verma"]')
user.click()


# time.sleep(5)
for i in range(10):
    testinput = driver.find_element(By.XPATH , '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    testinput.send_keys(data)
    testinput.send_keys(Keys.RETURN)

