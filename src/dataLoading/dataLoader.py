from src.common.configuration.conf import DataLoadingConfigurationEntries, process_type_configurations
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter


class DataLoader:
    def __init__(self, configuration):
        self.data_file_path = configuration.get_entry(DataLoadingConfigurationEntries.DATA_FILEPATH.value)
        self.test_set_percentage = float(configuration.get_entry(DataLoadingConfigurationEntries.TEST_SET_PERCENTAGE.value))
        self.splited_data_names = {}
        for process_type_configuration in list(process_type_configurations[configuration.get_entry(DataLoadingConfigurationEntries.SPLIT_TYPE.value)]):
            process_type_configuration_name = str(process_type_configuration).split(".")[1]
            print(process_type_configuration_name)
            print(process_type_configuration.value)
            print(configuration.get_entry(process_type_configuration.value))
            self.splited_data_names[process_type_configuration_name] = configuration.get_entry(process_type_configuration.value)

    def load(self, encoding="ISO-8859-1"):
        pass

    def preprocess(self, dataset):
        for splited_data_names_key in self.splited_data_names.keys():
            dataset.add_splited_data(splited_data_names_key, self.splited_data_names[splited_data_names_key])

        return TrainTestSplitter.split(dataset, self.test_set_percentage)
