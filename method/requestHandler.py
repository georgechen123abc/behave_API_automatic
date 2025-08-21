import requests
import logging
from method.getPath import getPath
import json
from  method.readYaml import yamlHandel
from jsonpath_ng import parse
from glom import glom
from string import Template


class RequestHandler:
    def __init__(self):
        print("start to upload the enviroment parameter")
        config = yamlHandel(getPath().get_envinfo_path()+"/env.yaml").read_yaml()
        '''
        Loop get the environment parameter and set attributes
        '''
        for section, values in config.items():
            if isinstance(values, dict):
                if section == 'static':
                    for key, value in values.items():
                        setattr(self, key, value)
            else:
                setattr(self, section, values)

        self.session = requests.Session()
        print("Finished")
        print(self.base_url)
        print(self.__dict__)
    def send_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        发送 HTTP 请求
        :param method: GET / POST / PUT / DELETE
        :param endpoint: 接口路径（不需要包含 base_url）
        :param kwargs: requests 的参数，如 json, params, data, headers
        :return: Response 对象
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logging.info(f"请求方法: {method}")
        logging.info(f"请求 URL: {url}")
        logging.info(f"请求参数: {kwargs}")



        try:
            response = self.session.request(method=method.upper(), url=url, timeout=10, **kwargs)
            print(f"statusCode: {response.status_code}")
            print(f"Response body: {response.text}")
            #print(f"header: {response.headers}")
            return response
        except requests.RequestException as e:
            logging.error(f"error: {e}")
            raise

    def read_json(self, json_file_name):
        with open(getPath().get_request_path()+f"/{json_file_name}") as f:
            data = json.load(f)
            try:
                body = data['body']
                payload = data['endpoint']
                parms = data['parameters']
            except KeyError as e:
                logging.error(f"Please make sure json format is correct: {e}")
            return body, payload, parms




    def get(self,json_file_name:str=None,json_data:dict = None) -> requests.Response:
        if json_file_name:
            request_data = self.read_json(json_file_name)
            body = request_data[0]
            endpoint = request_data[1]
            parameters = request_data[2]
            return self.send_request("GET", endpoint=endpoint,params=parameters )
        if json_data:
            body = json_data["body"]
            endpoint = json_data["endpoint"]
            parameters = json_data["parameters"]
            return self.send_request("GET", endpoint=endpoint, params=parameters)


    def post(self, json_file_name:str= None, json_data:dict = None) -> requests.Response:
        if json_file_name:
            request_data =  self.read_json(json_file_name)
            body = request_data[0]
            endpoint = request_data[1]
            parameters = request_data[2]
            return self.send_request("POST", endpoint=endpoint, json=body)
        if json_data:
            body = json_data["body"]
            endpoint = json_data["endpoint"]
            parameters = json_data["parameters"]
            return  self.send_request("POST", endpoint=endpoint, json=body)



    def get_response(self,data, jsonpath):
        try:
            jsonpath_expr = glom(data,jsonpath)
            if not jsonpath_expr:
                raise ValueError(f"No match found for JSONPath: {jsonpath}")
            return jsonpath_expr

        except Exception as e:
                raise RuntimeError(f"JSONPath parsing error111: {e}")

    def set_dynamic_value(self,data,jsonpath,dynamic_value):
        self.dynamic_data = {}
        self.value = self.get_response(data,jsonpath)
        print(self.value)
        config = yamlHandel(getPath().get_envinfo_path() + "/env.yaml").read_yaml()
        for section, values in config.items():
            if section == 'dynamic':
                for key in values.keys():
                    self.dynamic_data[key] = ""

        self.dynamic_data[dynamic_value] = self.value

        print(self.dynamic_data.items())
        return self.dynamic_data






if __name__ == '__main__':
    json = {
  "body": {},
  "endpoint": "/v1/rest/com/becn/orderdetail",
  "parameters": "account=280381&orderId=YD12345"

}
    RequestHandler().get(json_data=json)
















