Feature: Login

  Scenario: As a customer I can login with correct username and password
    When I use example.json API with POST
    Then the statusCode should be "200"
   # And I can get the correct response


