from behave import given,when,then
from googlePyrate.googleResults import GoogleResults

@given('a string for search')
def createAString(context):
	googleResults = GoogleResults()
	googleResults.forSearch = "scrapy"

@when('call the Google url')
def buildTheGoogleUrl(context):
	pass


