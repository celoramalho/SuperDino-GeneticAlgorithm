from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

class DinoGame:
    def __init__(self):
        self.driver = self._initialize_chrome()

    def _initialize_chrome(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def open_game(self):
        try:
            self.driver.get("chrome://dino")
            print("Dino game opened successfully.")
        except WebDriverException:
            pass

    def keep_open(self):
        print("Press Enter to close the browser...")
        input()
        
    def close(self):
        if self.driver:
            self.driver.quit()
            print("Browser closed successfully.")


#    game = DinoGame()
#    game.open_game()
#    game.keep_open()  # Keep the browser open
#    game.close()