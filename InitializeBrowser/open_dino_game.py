from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

def open_chrome():
    # Configure Chrome options
    chrome_options = Options()
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--disable-popup-blocking")
    #chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--enable-offline-mode")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver

driver = open_chrome()
try:
    driver.get("chrome://dino")
except WebDriverException:
    pass

#driver.get("chrome://dino")