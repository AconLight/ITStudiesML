import unittest

from src.common.configuration.conf import Configuration, ConfigurationType
from src.common.configuration.config_validator import ConfigurationError


class ConfigurationTests(unittest.TestCase):
    def test_raises_configuration_excetion_on_missing_entry(self):
        #given
        config_map = {}
        configuration = Configuration(ConfigurationType.DATALOADING, config_map)
        missing_entry_name = 'hello'

        #when
        #then -> throws exception
        with self.assertRaises(ConfigurationError):
            configuration.get_entry(missing_entry_name)

    # def