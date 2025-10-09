from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import threading
from concurrent.futures import ThreadPoolExecutor

link_list = ['https://www.google.com/',"https://www.google.com/"]


def multi_page_scrape(link):
    driver = webdriver.Chrome()
    driver.get(link)
    print(f"{threading.current_thread().name} scrapped")

with ThreadPoolExecutor(max_workers=2) as executor:
    execute = [executor.submit(multi_page_scrape,x) for x in link_list]
time.sleep(20)
