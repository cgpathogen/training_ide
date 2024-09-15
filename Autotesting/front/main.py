import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory":f"{os.getcwd()}\downloads"
}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--window-size=700,700")
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("--user-agent=Test_USer")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(options=chrome_options)


driver.get(url="https://bot.sannysoft.com/")



time.sleep(7)
print("done")
