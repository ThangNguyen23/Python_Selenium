import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

class MainPage:
    def __init__(self, driver):
        self.driver = driver
    
    def click_google_login_button(self):
        login_button = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Đăng nhập bằng Google"]')
        login_button.click()


class AppiumTest(unittest.TestCase):
    def setUp(self) -> None:
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Pixel 7 Pro API 33',
            appPackage='com.testing.certifications',
            appActivity='.MainActivity',
            language='en',
            locale='US'
        )

        appium_server_url = 'http://127.0.0.1:4723/wd/hub'
        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        self.driver = webdriver.Remote(command_executor = appium_server_url, options = capabilities_options)
        self.main_page = MainPage(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        self.main_page.click_google_login_button()


if __name__ == '__main__':
    unittest.main()
