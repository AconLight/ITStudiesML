from src.common.dataset import Dataset
from src.dataLoading.dataLoader import DataLoader
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
import pandas as pd
import os
class CsvDataLoader(DataLoader):
    def __init__(self, configuration):
        super().__init__(configuration)

    # Datasets may require encoding with retry with different encodings to load
    def load(self, encoding="ISO-8859-1"):
        try:
            print("database: " + self.data_file_path)
            data = pd.read_csv(self.data_file_path, encoding=encoding)
            data = data.dropna(subset=self.feedColumns + [self.classificationColumn])
            dataset = Dataset(data)
            dataset.set_data_columns(self.feedColumns)
            dataset.set_target_columns([self.classificationColumn])
            return dataset
        except FileNotFoundError:
            raise FileNotFoundError('Dataset file has not been found')
        except Exception as e:
            raise type(e)('Loading dataset with different encoding (utf-8, latin, ...) may help!')




