Feature: Login

  Background:
    Given home: I am a user on home page
    When home: I click bookstore application card
    When books: I click login button

  @smoke
  Scenario: I login with valid credentials
    When login: I login with user "Chivu23" and pass "Start12345!"
    Then books: I should land on books page


  @smoke
  Scenario Outline: I login with invalid credentials
    When login: I login with user "<user>" and pass "<pswd>"
    Then login: I validate that error message is displayed

Examples:

    | user     | pswd      |
    | Chivu23  | Test123   |
    | Chivu23  | Test1231  |

