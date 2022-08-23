#Author: Debashis

Feature: Test Angular Web page

  Background:
    Given the user is on "http://juliemr.github.io/protractor-demo/"

  @angular @demo
  Scenario: To verify functionality on a simple angular JS page
    When user enters "2" as "first" operand
    When user selects "%" as operator
    When user enters "2" as "second" operand
    When user clicks on go button
    Then correct expression and result should be displayed