from selenium.webdriver.common.by import By


class MainPageLocators:
    INPUT_SEARCH = (By.XPATH, '//input[@class="input__control input__input"]')
    SEARCH_BUTTON = (By.XPATH, '//div[@class="search2__button"]')
    SEARCH_BUTTON_2 = (By.XPATH, '//div[@class= "service service_name_search"]')
    FOUND_STRING = (By.XPATH, '//div[@class = "organic__url-text"]')
