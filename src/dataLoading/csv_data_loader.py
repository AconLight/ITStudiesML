from src.dataLoading.dataLoader import DataLoader
import pandas as pd

class CsvDataLoader(DataLoader):
    def __init__(self, configuration):
        super().__init__(configuration)

    # Datasets may require encoding with retry with different encodings to load
    def load(self, encoding="ISO-8859-1"):
        try:
            return pd.read_csv(self.data_file_path, encoding="ISO-8859-1")
        except Exception as e:
            raise type(e)(e.message + ' Loading dataset with different encoding (utf-8, latin, ...) may help!')



