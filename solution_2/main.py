import json
from solution_2.data_etl import *


with open("./solution_2/data_etl/module.json") as infile:
    module_json = json.load(infile)
infile.close()


def _get_etl_by_datasource_name(datasource_name): 
    solution_name, dir_name, module_name, class_name  = module_json[datasource_name].rsplit('.', 3)
    module_path = ".".join([solution_name, dir_name, module_name])
    module = __import__(module_path, fromlist=[class_name])
    klass = getattr(module, class_name)
        
    return klass


def transform_data(datasource_name):
    klass = _get_etl_by_datasource_name(datasource_name)
    transformer = klass()

    transformer.transform()
