import unittest

from src.common.configuration.conf import Configuration, ConfigurationType
from src.dataLoading.csv_data_loader import CsvDataLoader


class DataLoaderTests(unittest.TestCase):
    def test_csv_dataset_loading(self):
        #given
        config_map = {'data_file_path' : 'test/data/Speed-Dating-Data.csv'}
        configuration = Configuration(ConfigurationType.DATALOADING, config_map)
        data_loader = CsvDataLoader(configuration)

        #when
        data = data_loader.load()

        #then
        self.assertNotEqual(data.shape, None)