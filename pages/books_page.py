from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys


class BooksPage(BasePage):
    # SELECTORS_____
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_BOOKS = '//div[@class="action-buttons"]'
    SEARCH_INPUT = '//input[@id="searchBox"]'
    BOOK_TITLE = '//div[@class="action-buttons"]//a'
    ADD_TO_YOUR_COLLECTION_BUTTON = '(//button[@id="addNewRecordButton"])[2]'
    BACK_TO_BOOK_STORE_BUTTON = '(//button[@id="addNewRecordButton"])[1]'

    # ACTIONS_____
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
        sleep(3)

    def click_add_to_your_collection_button(self):
        self.wait_for_elem(self.ADD_TO_YOUR_COLLECTION_BUTTON)
        self.driver.find_element(By.XPATH, self.ADD_TO_YOUR_COLLECTION_BUTTON).click()
        sleep(3)

    def click_back_to_book_store_button(self):
        self.wait_for_elem(self.BACK_TO_BOOK_STORE_BUTTON)
        self.driver.find_element(By.XPATH, self.BACK_TO_BOOK_STORE_BUTTON).click()
        sleep(2)

    def fill_search_input(self, query):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.clear()
        search.send_keys(query)

    def clear_search_input(self):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.send_keys(Keys.CONTROL, 'a')
        search.send_keys(Keys.BACKSPACE)

    def click_book_by_title(self, title):
        self.driver.find_element(By.XPATH, '//a[text()="' + title + '"]').click()

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
