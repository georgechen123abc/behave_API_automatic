import os



class getPath:
    def __init__(self,env="prod"):
        self.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if env == "prod" or env == 'uat':
            self.env=env
        else:
            raise Exception(f"Unknown environment: {env}")
    def get_envinfo_path(self):
        envinfo_path =  self.root_dir+f"/data/{self.env}/env_info"
        return envinfo_path

    def get_request_path(self):
        request_path = self.root_dir+f"/data/{self.env}/request"
        return request_path

    def get_util_path(self):
        util_path = self.root_dir+"/method"
        return util_path
    def get_log_path(self):
        log_path = self.root_dir+"/log"
        return log_path





if __name__ == '__main__':
    print(getPath().get_envinfo_path())
    getPath().get_request_path()