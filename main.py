import time

from browsers import ChromeDriverFactory, EdgeDriverFactory
from browsers_handler import BrowserHandler

class MainApplication:
    def run(self):
        try:
            edge_tests = BrowserHandler(EdgeDriverFactory())
            edge_tests.run_tests()
            
            chrome_tests = BrowserHandler(ChromeDriverFactory())
            chrome_tests.run_tests()
            
        except Exception as e:
            print(f"Your error: {e}")

if __name__ == "__main__":
    app = MainApplication()
    app.run()
    