import enum
from csv import reader
from os import getcwd, sep

from src.common.configuration.config_validator import ConfigurationValidator

cwd = getcwd()

columnSplitter = "^"


def parse_add_conf(conf, path):
    with open(cwd.split("src" + sep + "main")[0] + "conf" + sep + path, newline='') as csv_file:
        conf_reader = reader(csv_file, delimiter=' ', quotechar='|')
        for row in conf_reader:
            columns = row[1].split(columnSplitter)
            if len(columns) < 2:
                conf.update({row[0]: row[1]})
            else:
                conf.update({row[0]: columns})
    return conf


class ConfigurationLoader():
    @staticmethod
    def parse_add_conf(conf, path, configuration_type):
        with open(cwd.split("src" + sep + "main")[0] + "conf" + sep + path, newline='') as csv_file:
            conf_reader = reader(csv_file, delimiter=' ', quotechar='|')
            for row in conf_reader:
                columns = row[1].split(columnSplitter)
                if len(columns) < 2:
                    conf.update({row[0]: row[1]})
                else:
                    conf.update({row[0]: columns})
        return Configuration(configuration_type, conf)

class Configuration():
    def __init__(self, configuration_type, configuration_map) -> None:
        super().__init__()
        self.config = configuration_map
        self.type = configuration_type

    def get_entry(self, entry_name):
        if self.config == None:
            raise TypeError("Configuration object has not been set")

        return ConfigurationValidator.return_value_if_configuration_entry_exists(self.config, entry_name)



class ConfigurationType(enum.Enum):
   DATALOADING = "DataLoading"
   CLASSIFICATION = "Classification"
   EVALUATION = "Evaluation"