from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# ua = UserAgent()
# user_agent = ua.random
# print(f"Using User-Agent: {user_agent}")
# chrome_options.add_argument(f"user-agent={user_agent}")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/')

driver.maximize_window()

google_input = driver.find_element(By.NAME,'q')
google_input.send_keys("Laptop Shop Near Mirpur")
google_input.send_keys(Keys.RETURN)
time.sleep(30)
# recaptcha_checkbox = driver.find_element(By.CLASS_NAME, "g-recaptcha")
# action = ActionChains(driver)
# action.move_to_element(recaptcha_checkbox).click().perform()

time.sleep(50)
