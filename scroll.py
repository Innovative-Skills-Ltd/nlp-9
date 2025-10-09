from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.daraz.com.bd/products/parachute-coconut-oil-easy-jar-350ml-50ml-free-i513892555-s2468572072.html')

driver.maximize_window()

height = driver.execute_script('return document.body.scrollHeight')

print(height)

for i in range(0,height+1300,60):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

comments = driver.find_elements(By.CLASS_NAME,'content')

total_button = driver.find_elements(By.CLASS_NAME,'next-pagination-item')

print(len(total_button))

# all_cmt = []
# for i in comments:
#     all_cmt.append(i.text)

# print(all_cmt)
time.sleep(20)

