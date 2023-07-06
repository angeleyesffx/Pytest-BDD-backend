Feature: Example Post API
    As a user from I want to test API Services

    Scenario Outline: Send a valid request to the API
        Given an user from the country <country> with the valid credential
        When the user choose the entity <service> and the API method <method> - <version>
        And the user prepare the request using <scenario> information
        And the user get a valid token
        And the user send the request
        Then the status response to the valid request should be status: 202

        Examples: Settings
        | country | service   | method | version | scenario   |
        | br      | register | post    | v1      | valid data |


    Scenario Outline: Send a invalid request to the API
        Given an user from the country <country> with the valid credential
        When the user choose the entity <service> and the API method <method> - <version>
        And the user prepare the request using <scenario> information
        And the user get a valid token
        And the user send the request
        Then the status response to the invalid request should be status: 400

        Examples: Settings
        | country | service     | method | version | scenario   |
        | br      | register   | post    | v1      |invalid data|
        | br      | register   | post    | v1      |empty data  |

    Scenario Outline: Send a GET request to the API
        Given an user from the country <country> with the valid credential
        When the user choose the entity <service> and the API method <method> - <version>
        And the user prepare the request using <scenario> information
        And the user get a valid token
        And the user send the request
        Then the status response to the valid request should be status: 200

        Examples: Settings
        | country | service    | method | version | scenario   |
        | br      | register   | get    | v1      | valid data |
