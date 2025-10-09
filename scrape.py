from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #client

driver.get('https://www.daraz.com.bd/manual-juicers/')



driver.maximize_window()
text_list = []
for i in range(1,3):
    j = str(i)
    text = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/span['+j+']').text
    text_list.append(text)

print(text_list)

link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')

print(link)
driver.get(link)
driver.maximize_window()

#scrape a image and download the image

time.sleep(10)


