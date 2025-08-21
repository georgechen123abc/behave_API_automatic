from glom import glom
from method.getPath import getPath
from  method.readYaml import yamlHandel
from method.requestHandler import RequestHandler
import json
import logging
import re
from string import Template

class set_dynamic_parameter:
    def __init__(self):
            self.dynamic_data={}
            config = yamlHandel(getPath().get_envinfo_path() + "/env.yaml").read_yaml()
            for section, values in config.items():
                if section == 'dynamic':
                    for k,v in values.items():
                        self.dynamic_data[k] = v

            #self.dynamic_data[dynamic_value] = self.value

            print(self.dynamic_data)


    def get_response(self,data,jsonpath):
        try:
            jsonpath_expr = glom(data,jsonpath)
            if not jsonpath_expr:
                raise ValueError(f"No match found for JSONPath: {jsonpath}")
            return jsonpath_expr

        except Exception as e:
                raise RuntimeError(f"JSONPath parsing error: {e}")

    def set_dynamic_value(self,data,jsonpath,dynamic_value):
        self.value = self.get_response(data,jsonpath)
        self.dynamic_data[dynamic_value] = self.value
        return self.dynamic_data

    def get_dynamic_key_from_json(self,jsonname):
        with open(getPath().get_request_path() + f"/{jsonname}") as f:
            data = json.load(f)
            try:
                body = data['body']
                payload = data['endpoint']
                parms = data['parameters']
            except KeyError as e:
                logging.error(f"Please make sure json format is correct: {e}")


    def set_dynamic_parameter(self,jsonname,dynamic_value):
        with open(getPath().get_request_path() + f"/{jsonname}") as f:
            data = json.load(f)
        #var = {'orderId': 'ST01968', 'userId': '', 'accountId': '280381'}
        template = Template(data["parameters"])
        dynamic_parameter = template.substitute(dynamic_value)
        data["parameters"] = dynamic_parameter
        return data



















