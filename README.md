#R egression Test Counter

### Function:
To count existing regression tests for as many services as needed so that accurate test coverage can be reported on a monthly basis.

### What makes a test case?

Let's look at what this program considers to be a test case.
<br>
Example 1:
```
Feature: Wex Status: Invalid Login Credentials

  Scenario: Invalid Login Credentials
    When I go to WEX_STATUS_URL
    Then I click on the Wex Status sign in button
    Then I click Sign in with Okta
    And I enter an invalid Okta username and password and click login
    Then I will see an error message
```
The scenario above will count as <b>1</b> test case.
<br>

Example 2:
```
  Scenario Outline: Happy Path - Schedule Maintenance
    Given I click on the Actions button for QA Testing
    Then I click on Schedule Maintenance
    Then I click on notify users
    And I enter a subject, start and stop dates and times, and a <description>
    And I click submit
    Then I verify that the new maintenance event is present on the page
    When I click on QA Test 1
    Then I verify the new maintenance event is not present on the page
    Then I logout
    Examples:
     | description                    |
     | QA Test - Schedule Maintenance |
```
The scenario above will count as <b>1</b> test case.


Example 3: 
```
  Scenario Outline: Schedule Maintenance - Impacted Platforms
    Given I click on the Actions button for QA Testing
    And I click on the New Incident button
    Then I enter a notification subject, future date and time, and a <description>
    And I select the priority to <priority>
    Then I select <impact> for Incident Impact Clients
    And I enter <client> for client impacted
    Then I click submit button
    And The newly created incident should be present
    Then I logout
    Examples:
    |priority|description                                                |client     |impact  |
    |P4      |QA Test - Schedule Maintenance - Client Impact - "Yes"     |AMEX       |yes     |
    |P4      |QA Test - Schedule Maintenance - Client Impact - "Possible"|FNBO       |possible|
    |P4      |QA Test - Schedule Maintenance - Client Impact - "Yes"     |ALL_CLIENTS|yes     |
    |P4      |QA Test - Schedule Maintenance - Client Impact - "Possible"|ALL_CLIENTS|possible|
```
This will count as 4 test cases because it will run <b>4</b> times for each of the examples.


### Code
#### github.py:
* The file `github.py` contains class GithubPull. This class contains only one function, and that is to perform `git pull` on any of the directories you put in `self.root_dict`. These paths must be the project root path in order to pull. 
  * Example: `/Users/w504327/tests/goTests/ps-cbs-address-service`.
* `def pull_changes` will count the length of your `root_dic` and run `git pull` for the number of paths you have listed in your dictionary. 


#### test_counter.py:
The file `test_counter.py` contains two dictionaries. 
* `self.path_dict` is where you will put the full path to where the feature files are. <br>
  * Example: `/Users/w504327/tests/goTests/ps-cbs-address-service/tests/features`.
  <br>
* `name_dict` is where you will put the name of the service. This dictionary was created to print the name as the tests are being counted. The keys and values in this dictionary should match the keys and values for `self.path.dict`. I've left the names in alphabetical order for ease of use. You can add more or less projects by adding a new sequential
key:value pair to both dictionaries.
* The `count_occurrences()` function will get the length of your `self.path_dict` and will count the number of scenarios and scenario examples for
each of the directories listed in that dictionary.

### To Run
In the terminal run: `python3 main.py`. You out output should look similar to this:
```Address Service Scenario: 0
 Scenario Outline: 29
 total:  29 

Apigee Manager Scenario: 0
 Scenario Outline: 24
 total:  24 

Auth Service Scenario: 0
 Scenario Outline: 24
 total:  24 
```

Scenario == the number of scenarios (no example table).
