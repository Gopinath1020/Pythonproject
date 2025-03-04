Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid credentials
    Given I open the OrangeHRM login page
    When I enter the username "Admin"
    And I enter the password "admin123"
    And I click the login button
    Then I should be redirected to the dashboard
