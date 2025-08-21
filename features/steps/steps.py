from behave import given, when, then


@then("I put {value} into the {dynamic_key}")
def step_put_into_dynamic_key(context,value,dynamic_key):
    try:
        response = context.response.json()
        context._root["shared_data"] = context.dynamic.set_dynamic_value(data=response,jsonpath=value,dynamic_value=dynamic_key)
        print(context._root["shared_data"])
    except Exception as e:
            print(e)


@when("I use {apiName} API with {requestMethod}")
def step_use_api(context, apiName, requestMethod):
    context.apiName = apiName
    context.requestMethod = requestMethod
    try:
        if requestMethod == "GET":
            context.response = context.client.get(apiName)
        if requestMethod == "POST":
            context.response = context.client.post(apiName)
        return context.response.json(),context.apiName,context.requestMethod
    except Exception as e:
        print(e)




@when("I set {value} into {json_file_name}")
def step_set_dynamic_value(context,value,json_file_name):
    try:
        dynamic_params = context._root["shared_data"]
        print(dynamic_params)
        context.request = context.dynamic.set_dynamic_parameter(dynamic_value=dynamic_params,jsonname=json_file_name)
        print(context.request)
        return context.request
    except Exception as e:
        print(e)




