from selenium import webdriver

import time
from selenium.webdriver.common.keys import Keys

# Creating a Firefox object
# driver = webdriver.Firefox()

driver = webdriver.Chrome("C:/chromedriver")
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://www.amazon.in/")
time.sleep(3)

driver.find_element_by_name("field-keywords").send_keys("mobiles")
data = driver.find_element_by_id(
    "nav-search-submit-button").send_keys(Keys.ENTER)
print(data)
time.sleep(10)
driver.quit()
print("Succesfully Completed")
