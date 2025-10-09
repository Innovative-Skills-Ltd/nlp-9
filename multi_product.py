#two types button pagination
#one: on-load pagination
#two: on-render pagination
#scroll pagination
#show more/next pagination

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

import math
total_pages = '815 items found for "hoses pipes"'
#find out number from a string using regex
t_page = total_pages.split()[0]
t_page_num = math.ceil(int(t_page)/40)
print(t_page_num)

text_list = []
for page in range(1,t_page_num+1):
    p = str(page)
    driver.get(f'https://www.daraz.com.bd/hoses-pipes/?page={p}')
    driver.maximize_window()
    for i in range(1,41):
        j = str(i)
        text = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
        text_list.append(text)


print(text_list)
print(len(text_list))


time.sleep(20)
driver.quit()