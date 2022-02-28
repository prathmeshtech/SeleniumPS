from distutils.filelist import findall
from selenium import webdriver

import csv
import time
from selenium.webdriver.common.keys import Keys

# Creating a Chrome object
driver = webdriver.Chrome("C:/chromedriver")
driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://www.amazon.in/")
time.sleep(3)

driver.find_element_by_name("field-keywords").send_keys("mobiles")
driver.find_element_by_id("nav-search-submit-button").send_keys(Keys.ENTER)

myFile = open('Amazon_values.csv', 'w')
with myFile:
    myAmazon = ['mobile_name', 'Price', 'Rating']
    writer = csv.DictWriter(myFile, fieldnames=myAmazon)
    writer.writeheader()
    writer.writerow({'mobile_name': 'Samsung M12',
                    'Price': '12000', 'Rating': '4.1'})
    writer.writerow({'mobile_name': 'Motorola E4 plus',
                    'Price': '10000', 'Rating': '4.5'})
time.sleep(3)
driver.quit()
print("Succesfully Completed")
