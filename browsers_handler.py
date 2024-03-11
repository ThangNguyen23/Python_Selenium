import time

class BrowserHandler:
    @staticmethod
    def open_and_maximize(driver, url):
        driver.get(url)
        driver.maximize_window()
    
    @staticmethod 
    def quit_browser(driver):
        time.sleep(5)
        driver.quit()