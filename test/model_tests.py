from unittest import TestCase

from src.common.configuration.conf import DataLoadingConfigurationEntries
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
from src.modelProcessing.modelAlgorithms.algorithms.naive_bayes import NaiveBayes
from test.data.datasets_object_mother import DatasetsObjectMother


class ModelTests(TestCase):
    def test_naive_bayes_for_encoded_columns(self):
        # given
        configuration = DatasetsObjectMother.speed_dating_csv_configuration
        # data_loader = CsvDataLoader(configuration)
        # dataset = data_loader.load()
        dataset = DatasetsObjectMother.students_dataset_with_encoded_columns
        dataset.drop_column('Name')
        dataset.set_data_columns(['Age', 'City'])
        dataset.set_target_columns(['Country'])
        X_train, Y_train, X_test, Y_test = TrainTestSplitter.split(dataset, float(
            configuration.get_entry(DataLoadingConfigurationEntries.TEST_SET_PERCENTAGE.value)))

        model = NaiveBayes()

        # when
        model.train(X_train, Y_train)
        Y_pred = model.predict(X_test)

        # then
        print()