#CPU = logical core = 8*2 =  # 16 workers - CPU Limit
#ram = 12 workers
#recommned = min(cpu,ram)

import multiprocessing
import psutil
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def selenium_measure():
    driver = webdriver.Chrome()
    time.sleep(2)
    pid = driver.service.process.pid
    ram_pid = psutil.Process(pid)
    final_ram_process = ram_pid.memory_info().rss
    print(final_ram_process)

    for child in ram_pid.children(recursive=True):
        print(child,child.memory_info().rss)
        final_ram_process = final_ram_process+child.memory_info().rss
    return final_ram_process

 
def estimate_workers():
    logical_cores = multiprocessing.cpu_count()
    max_cpu = logical_cores * 1.5
    ram_gb = psutil.virtual_memory().total/(1024**3)
    ram_selenium = selenium_measure()/(1024**3)

    max_ram = ram_gb/ram_selenium

    safe_usage = min(max_ram,max_cpu)
    print(logical_cores,max_cpu,ram_selenium,ram_gb,safe_usage)

estimate_workers()
