# Framework-completed-Automat-Testing-with-Python
### Design Pattern: POM (page object model)

POM - CHANGES ARE MADE ONLY IN ONE PLACE - ELEMENTS BY CLASSES

(each page has a specific class where we find elements specific to those pages, then the actions that can be done on that page.)

 The files "browser" and "context" create the class of the Browser with the initialization browser and wait.
 The "context" file contains 2 methods: one that is called before each test, and another at the end of each test.

Gherkin : 
1. given - set initial 
2. when - action
3. then - final check 

Concept BDD - Behavior-Driven Development
( use Gherkin syntax for standardize team communication )

 Steps folder define with Gherkin syntax.

 The features file in which we test a logging capability with a positive, then negative test case