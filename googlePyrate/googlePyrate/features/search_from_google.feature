Feature: Integration with Google

Scenario: Search something accessing Google Search
	Given a string for search
	When call the Google url
    Then it receive the set of results by html
    But it receive a invalid result
    But it receive a set of tags with results
