Feature: Books capability

 Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with user "Chivu23" and pass "Start12345!"

  @regression
  Scenario: I login with stock count
    Then books: I validate that 8 books are displayed

  @regression
  Scenario Outline: I validate the search is working
    When books: I search after "<query>"
    Then books: I validate that only "Git Pocket Guide" book is displayed

  Examples:
    |query   |
    |Git     |
    |Richard |

  @test
  Scenario: I validate that clear search is working
    When books: I search after "azi e azi, o zi frumoasa"
    When book: I clear search input
    Then books: I validate that 8 books are displayed
