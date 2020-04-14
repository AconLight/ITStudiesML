import itertools

from src.common.dataset import Dataset
from src.dataLoading.dataLoader import DataLoader
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
import pandas as pd
import os
class CsvDataLoader(DataLoader):
    def __init__(self, configuration, file):
        super().__init__(configuration)
        self.file = file

    # Datasets may require encoding with retry with different encodings to load
    def load(self, encoding="ISO-8859-1"):
        try:
            self.file.write("database: " + self.data_file_path + '\n')
            data = pd.read_csv(self.data_file_path, encoding=encoding)
            sub = list(itertools.chain(*self.splited_data_names.values()))
            print("sub")
            print(sub)
            data = data.dropna(subset=sub)
            dataset = Dataset(data)
            return self.preprocess(dataset)
        except FileNotFoundError:
            raise FileNotFoundError('Dataset file has not been found')
        except Exception as e:
            raise type(e)('Loading dataset with different encoding (utf-8, latin, ...) may help!')


