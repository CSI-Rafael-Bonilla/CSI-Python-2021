import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Locate webdriver path. 
myPath = Path(__file__).parents[0]
driverPath = f"{myPath}/chromedriver"

# Prevent window from opening. Background Task
options = Options()
#options.headless = True

#Contruct webdriver (executable_path is now deprecated)
driver = webdriver.Chrome(executable_path=driverPath, options = options)

# Open URL
driver.get("https://www.sanignacio.pr/")

#Find and print price element value. 
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# print(price)
# driver.close()


# driver.maximize_window()
# driver.find_element(By.NAME, 'q').send_keys('Baauer')
# driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)