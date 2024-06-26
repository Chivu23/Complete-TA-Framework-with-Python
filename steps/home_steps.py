from pages.home_page import HomePage
from behave import *

# given - set initial situation
# when - intermediate actions
# then - final check


home_page = HomePage()


@given('home: I am a user on home page')
def step_impl(context):
    home_page.driver.delete_all_cookies()
    home_page.navigate_to_home_page()


@when('home: I click bookstore application card')
def step_impl(context):
    home_page.click_book_store_application_card()


