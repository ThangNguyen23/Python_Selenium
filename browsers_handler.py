import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed

class BrowserHandler:
    def __init__(self, driver):
        self.driver = driver.create_driver()
    
    def open_and_maximize(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.refresh()
        except Exception as e:
            print(f"Your error: {e}")
    
    def quit_browser(self):
        try:
            time.sleep(5)
            self.driver.quit()
        except Exception as e:
            print(f"Your error: {e}")
        
    def click_element(self, element_name, value_of_element):
        try:
            # element = WebDriverWait(self.driver, 10).until(
            #     EC.element_to_be_clickable((getattr(By, element_name), value_of_element))
            # )
            # element.click()
            self.driver.find_element(getattr(By, element_name), value_of_element).click()
        except Exception as e:
            print(f"Your error: {e}")
            
    def run_tests(self):
        try:
            self.open_and_maximize("https://www.facebook.com/")
            self.click_element("XPATH", "//a[contains(text(), 'Create new account')]")
            
            self.quit_browser()
            
            print("Test passed")
            return 0
        except Exception as e:
            print(f"Your error: {e}")
            return 1
    
    @staticmethod
    def run_multi_threads(self, test_func):
        with ThreadPoolExecutor(max_workers = len(test_func)) as executor:
            futures = [executor.submit(test) for test in test_func]
            
            results = []
            for future in as_completed(futures):
                results.append(future.result())
            
            return results