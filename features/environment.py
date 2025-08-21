from method.requestHandler import RequestHandler
from method.assertHandler import AssertHandler
from method.setDynamicParameter import set_dynamic_parameter
import logging
import os
from method.getPath import getPath
from datetime import datetime
from colorama import Fore,Style
import allure
import json


log_dir = getPath().get_log_path()
log_file = os.path.join(log_dir,f"behave_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def before_all(context):
    try:
        print("Before all")
        context.client = RequestHandler()
        context.dynamic = set_dynamic_parameter()
        context.client.post("login.json")
        context._root["shared_data"] = {}


    except Exception as e:
        # 打印详细异常并抛出，Behave 会报错
        print(f"Failed to initialize RequestHandler: {e}")
        raise e

def before_scenario(context, scenario):
    logging.info("Scenario name ------" + scenario.name)


def after_scenario(context, scenario):
    if context.apiName and context.requestMethod:
        with open(getPath().get_request_path() + f"/{context.apiName}") as f:
            data = json.load(f)
        if context.requestMethod.upper() == "POST":
                try:
                    body = json.dumps(data['body'])
                    allure.attach(body,name="Request body",attachment_type=allure.attachment_type.JSON)
                except KeyError as e:
                    logging.error(f"Please make sure json format is correct: {e}")

        if context.requestMethod.upper() == "GET":
            parameter = data["parameters"]
            allure.attach(parameter,name="Request parameter",attachment_type=allure.attachment_type.TEXT)
    response = json.dumps(context.response.json(),indent=2)
    status_code = context.response.status_code
    allure.attach( response,name="Response body",attachment_type=allure.attachment_type.JSON)

    if str(scenario.status.name) == "passed":
        symbol = Fore.GREEN + "✅" + Style.RESET_ALL
    elif str(scenario.status.name) == "failed":
        symbol = Fore.RED + "❌" + Style.RESET_ALL
    else:
        symbol = Fore.YELLOW + "⚠️" + Style.RESET_ALL
    logging.info(f"{scenario.name} test result ------{symbol}")


    def after_all(context):
        logging.info(f"Start to clear test data")



