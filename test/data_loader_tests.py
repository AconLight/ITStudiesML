import unittest

from src.common.configuration.conf import Configuration, ConfigurationType
from src.dataLoading.csv_data_loader import CsvDataLoader
from test.data.datasets_object_mother import DatasetsObjectMother


class DataLoaderTests(unittest.TestCase):
    def test_csv_dataset_loading(self):
        #given
        configuration = DatasetsObjectMother.speed_dating_csv_configuration
        data_loader = CsvDataLoader(configuration)

        #when
        dataset = data_loader.load()

        #then
        self.assertNotEqual(dataset, None)