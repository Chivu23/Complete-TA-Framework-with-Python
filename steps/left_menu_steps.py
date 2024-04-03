from pages.left_menu import LeftMenu
from behave import *
from time import sleep

left_menu = LeftMenu()  # object of type BooksPage" to find actions


@when('menu: I click profile_section')
def step_impl(context):
    left_menu.click_profile_section()

