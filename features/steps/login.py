from behave import given, when, then
import sys
import os
from method.requestHandler import RequestHandler
from method.assertHandler import AssertHandler
import json



@when('I use login API with correct username and password')
def step_when_login(context):

        context.response = context.client.post("login.json")





@then('the statusCode should be "{status_code:d}"')
def step_then_result(context,status_code):
    try:
        AssertHandler.equal(context.response.status_code,status_code)
    except AssertionError as e:
        print(e)


