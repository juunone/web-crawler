import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.naver.com/')

query = driver.find_element_by_id('query').send_keys('맥북프로')
driver.find_element_by_id("search_btn").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".question a")))

results = driver.find_elements(By.CSS_SELECTOR,".question a")

for item in results:
    print(item.text)