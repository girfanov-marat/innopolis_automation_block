from locators.locators import MainPageLocators
from web.client import MainPage


def test_page(input_str: str) -> None:
    main_page = MainPage()
    main_page.open_page()
    main_page.input_to_search(input_str)
    main_page.wait.until(main_page.ex.presence_of_element_located(main_page.found_string))
    res = main_page.get_page_source()
    assert input_str in res
    main_page.quit_driver()


def test_press_to_element() -> None:
    main_page = MainPage()
    main_page.open_page()
    main_page.input_to_search('')
    locator = MainPageLocators.SEARCH_BUTTON_2
    main_page.press_to_element(locator, 5)
    main_page.quit_driver()


if __name__ == "__main__":
    test_page('Python')
    # test_press_to_element()
