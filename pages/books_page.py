from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class BooksPage(BasePage):
    # SELECTORS_____
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_BOOKS = '//div[@class="action-buttons"]'
    SEARCH_INPUT = '//input[@id="searchBox"]'
    BOOK_TITLE = '//div[@class="action-buttons"]//a'

    # ACTIONS_____
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def fill_search_input(self, query):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.clear()
        search.send_keys(query)
    # VALIDATIONS_____

    def validate_correct_url(self):
        sleep(1)
        expected = 'https://demoqa.com/books'
        actual_number = self.driver.current_url
        self.assertEqual(expected, actual_number, 'Url is incorrect')

    def validate_books_count(self, expected_number):
        sleep(1)
        actual = len(self.driver.find_elements(By.XPATH, self.NUMBER_BOOKS))
        self.assertEqual(expected_number, actual, 'Number of books incorrect')

    def validate_book_title(self, expected_title):
        self.wait_for_elem(self.BOOK_TITLE)
        actual_title = self.driver.find_element(By.XPATH, self.BOOK_TITLE).text
        self.assertEqual(expected_title, actual_title, 'Book title is  incorrect')