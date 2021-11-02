import os
import json
import dagbase
filedir = "./dag-configs/"
file_name = "test.json"
outputdir = "./dagbag/"

def read_wanted_values(filedir, filename):
    with open(filedir+filename , "r") as json_data:
        config_file = json.load(json_data)
        return config_file

def output_values(**config_file):
    lines = dagbase.dagbase
    base_config = config_file["extractor_config"]["base_config"]
    hello_function_configuration = config_file["extractor_config"]["hello_function_configuration"]
    second_function_configuration = config_file["extractor_config"]["second_function_configuration"]
    third_function_configuration = config_file["extractor_config"]["third_function_configuration"]
    hello_operator_config = config_file["extractor_config"]["hello_operator_config"]
    second_operator_config = config_file["extractor_config"]["second_operator_config"]
    third_operator_config = config_file["extractor_config"]["third_operator_config"]
    file_basic_config = lines.format(**base_config, **hello_function_configuration, 
    **hello_operator_config, **second_function_configuration, 
    **second_operator_config, **third_function_configuration, **third_operator_config)
    return file_basic_config

def write_output_to_file():
    for file in os.listdir(filedir):
       config_file = read_wanted_values(filedir, file)
       dag_output = output_values(**config_file)
       filedest = outputdir + config_file["extractor_config"]["py_file_config"]["dag_name"]
       with open(f"{filedest}", "w") as outputfile:
           outputfile.write(dag_output)

def main():
    write_output_to_file()

if __name__ == "__main__":
    main()