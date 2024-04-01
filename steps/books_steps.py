from pages.books_page import BooksPage
from behave import *

books_page = BooksPage()  # object of type BooksPage" to find actions


@when('books: I click login button')
def step_impl(context):
    books_page.click_login_button()


@then('books: I should land on books page')
def step_impl(context):
    books_page.validate_correct_url()


@then('books: I validate that 8 books are displayed')
def step_impl(context):
    books_page.validate_books_count(8)