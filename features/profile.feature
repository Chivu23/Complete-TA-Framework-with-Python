Feature: Profile capability

  @temp
  Scenario: I add/remove books to my collection
     Given home: I am a user on home page
     When home: I click bookstore application card
     When books: I click login button
     When login: I login with user "Chivu23" and pass "Start12345!"
     When books: I add to collection the book with title "Git Pocket Guy"
     When books: I add to collection the book with title "Speaking JavaScript"
     When menu: I click profile_section