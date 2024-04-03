from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LeftMenu(BasePage):
    # SELECTORS_____
    LOGIN_BUTTON = '//span[text()="Profile"]'

    # ACTIONS_____
    def click_profile_section(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        element = self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()
        self.driver.execute_script("arguments[0].click();", element)
