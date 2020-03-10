from src.dataLoading.dataLoader import DataLoader
import pandas as pd

class CsvDataLoader(DataLoader):
    def __init__(self, configuration):
        super().__init__(configuration)

    def load(self):
        return pd.read_csv(self.data_file_path)


