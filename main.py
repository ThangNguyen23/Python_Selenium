from browsers import ChromeDriverFactory, EdgeDriverFactory
from browsers_handler import BrowserHandler

class MainApplication:
    def run(self):
        factory = None
        browser = input("Enter the browser you want to use (Chrome or Edge): ").lower()
        
        if browser == "chrome":
            factory = ChromeDriverFactory()
        elif browser == "edge":
            factory = EdgeDriverFactory()
        else:
            raise ValueError("Browser not supported!")
        
        driver = factory.create_driver()
        
        handler = BrowserHandler()
        handler.open_and_maximize(driver, "https://www.google.com/")
        handler.quit_browser(driver)

if __name__ == "__main__":
    app = MainApplication()
    app.run()
    