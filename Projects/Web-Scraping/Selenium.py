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
driver.get("https://www.google.com/search?q=No+bitches%3F&rlz=1C5CHFA_enPR862PR862&sxsrf=APq-WBsl9Ei7ZhxqUtV3VVqgfBzKo_3v0g:1648654872426&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjJxJyAlu72AhUPEEQIHSFfArEQ_AUoAXoECAEQAw&biw=1280&bih=689&dpr=2#imgrc=qh3Qq3XswRvPQM")

#Find and print price element value. 
# price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# print(price)
# driver.close()


# driver.maximize_window()
# driver.find_element(By.NAME, 'q').send_keys('Baauer')
# driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)