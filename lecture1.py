from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.youtube.com/")
search = driver.find_element("name" , "search_query")
print(search)
search.send_keys("You see Big Girl reaction")
search.send_keys(Keys.RETURN)

print(driver.title)

time.sleep(10)

driver.quit()

