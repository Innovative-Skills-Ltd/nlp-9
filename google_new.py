from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from fake_useragent import UserAgent
import time

# --- Setup Chrome options ---
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Use random user agent from fake_useragent
ua = UserAgent()
user_agent = ua.random
print(f"Using User-Agent: {user_agent}")
chrome_options.add_argument(f"--user-agent={user_agent}")

# --- Initialize driver ---
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# --- Visit Google ---
driver.get('https://www.google.com')
time.sleep(5)

# --- Search something ---
google_input = driver.find_element(By.NAME, 'q')
google_input.send_keys("Laptop Shop Near Mirpur")
google_input.send_keys(Keys.RETURN)
time.sleep(10)

# --- Try to click reCAPTCHA (⚠️ this usually won’t work on Google SERP) ---
try:
    recaptcha_checkbox = driver.find_element(By.CLASS_NAME, "g-recaptcha")
    action = ActionChains(driver)
    action.move_to_element(recaptcha_checkbox).click().perform()
    print("Clicked reCAPTCHA checkbox.")
except Exception as e:
    print("reCAPTCHA element not found or not clickable:", e)

time.sleep(5)
driver.quit()
