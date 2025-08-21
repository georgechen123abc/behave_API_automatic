import yaml
import os

class yamlHandel:
     def __init__(self,yaml_file_path:str):
          if not os.path.exists(yaml_file_path) or not os.path.isfile(yaml_file_path):
               raise FileNotFoundError("File not found")
          self.file_path = yaml_file_path


     def read_yaml(self):
          with open(self.file_path, 'r') as stream:
               try:
                    data = yaml.safe_load(stream)
                    return data
               except yaml.YAMLError as exc:
                    print(exc)





