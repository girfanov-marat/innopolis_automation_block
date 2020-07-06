import time

import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from locators.locators import MainPageLocators

YANDEX_URL = 'http://www.ya.ru'


class MainPage:
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install()
    )
    wait = WebDriverWait(driver, timeout=5)
    ex = expected_conditions
    found_string = MainPageLocators.FOUND_STRING

    def open_page(self):
        self.driver.get(YANDEX_URL)

    def input_to_search(self, input_string: str):
        driver = self.driver
        driver.find_element(*MainPageLocators.INPUT_SEARCH).send_keys(input_string)
        driver.find_element(*MainPageLocators.INPUT_SEARCH).send_keys(Keys.ENTER)

    def get_page_source(self):
        return self.driver.page_source

    def press_to_element(self, locator, waiting_time=5):
        start_time = 0
        time_condition = True
        while time_condition:
            try:
                self.driver.find_element(*locator).click()
                time_condition = False
            except NoSuchElementException:
                time.sleep(0.5)
                start_time += 0.5
                if start_time == waiting_time:
                    raise Exception("Time out")
        # elem = WebDriverWait(self.driver, timeout=waiting_time).until(EC.presence_of_element_located(locator))
        # elem.click()

    def quit_driver(self):
        self.driver.quit()

