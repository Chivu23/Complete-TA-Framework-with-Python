Feature: books capability

 Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button
    When login: I login with user "Chivu23" and pass "Start12345!"

  @books
  Scenario: I login with stock count
    Then books: I validate that 8 books are displayed

  @test
  Scenario: I validate the search in working
    When books: I search after "GIT"
    Then books: I validate that only "Git Pocket Guide" book is displayed


