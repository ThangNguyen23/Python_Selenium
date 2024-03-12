import time

class BrowserHandler:
    def open_and_maximize(self, driver, url):
        driver.get(url)
        driver.maximize_window()
        driver.refresh()
    
    def quit_browser(self,driver):
        time.sleep(5)
        driver.close()
        driver.quit()