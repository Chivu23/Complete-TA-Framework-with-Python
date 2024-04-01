from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class BooksPage(BasePage):
    # SELECTORS_____
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_BOOKS = '//div[@class="action-buttons"]'

    # ACTIONS_____
    # def click_login_button(self):
    #     self.driver.get('https://demoqa.com')

    # def click_book_store_application(self):
    #     self.wait_for_elem(self.LOGIN_BUTTON)
    #     self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    # VALIDATIONS_____
    def validate_correct_url(self):
        sleep(1)
        expected = 'https://demoqa.com/books'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')

    def validate_books_count(self, expected_number):
        sleep(1)
        actual = len(self.driver.find_elements(By.XPATH, self.NUMBER_BOOKS))
        self.assertEqual(expected_number, actual, 'Number of books incorrect')
