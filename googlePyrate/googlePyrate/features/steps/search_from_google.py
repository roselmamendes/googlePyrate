from behave import given,when,then
from google_results import GoogleResults
import expected_results

@given('a string for search')
def createAString(context):
    context.googleResults = GoogleResults()
    context.toSearch = "scrapy"

@when('call the Google url')
def buildGoogleResults(context):
    context.result = context.googleResults.buildGoogleResults()

@then('it receive the set of results by html')
def receiveAResultByHtml(context):
    assert expected_results.EXPECTED_RESULT == context.result
