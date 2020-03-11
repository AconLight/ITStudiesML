from src.common.configuration.conf import DataLoadingConfigurationEntries


class DataLoader:
    def __init__(self, configuration):
        self.feedColumns = configuration.get_entry(DataLoadingConfigurationEntries.FEED_COLUMNS)
        self.classificationColumn = configuration.get_entry(DataLoadingConfigurationEntries.CLASSIFICATION_COLUMN)
        self.data_file_path = configuration.get_entry(DataLoadingConfigurationEntries.DATA_FILEPATH)


    def load(self, encoding="ISO-8859-1"):
        pass
