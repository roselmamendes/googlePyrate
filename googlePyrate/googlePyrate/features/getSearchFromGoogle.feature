Feature: Integration with Google

Scenario: Send the content for Google Search
	Given a string for search
	when call the Google url
	then it receive the result related with the string