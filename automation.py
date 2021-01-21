import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

executable_path = "/Users/melodyserra/Desktop/auto/chromedriver"

chrome_options = Options()
# chrome_options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=executable_path)
wait = WebDriverWait(driver, 10)

# visiting google homepage
print("- Visiting Google")
driver.get("https://www.google.com/")
