

class ConfigurationValidator:
    @staticmethod
    def return_value_if_configuration_entry_exists(config_map, entry_name):
        if entry_name not in config_map.keys():
            raise ConfigurationError("Missing entry \"" + entry_name + "\" in configuration " )
        return config_map[entry_name]

class ConfigurationError(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(ConfigurationError, self).__init__(message)