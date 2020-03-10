import copy
from unittest import TestCase

from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
from test.data.datasets_object_mother import DatasetsObjectMother


class PreprocessingTests(TestCase):
    def test_should_split_dataset(self):
        #given
        dataset = copy.deepcopy(DatasetsObjectMother.students_dataset)
        test_set_percentage = 1/6
        data_columns = ['Name', 'Age']
        target_columns = ['Country']
        dataset.set_data_columns(data_columns)
        dataset.set_target_columns(target_columns)

        #when
        X_train, Y_train, X_test, Y_test = TrainTestSplitter.split(dataset, test_set_percentage)

        #then
        self.assertEqual(X_train.shape[0], 5)
        self.assertEqual(Y_train.shape[0], 5)
        self.assertEqual(X_test.shape[0], 1)
        self.assertEqual(Y_test.shape[0], 1)

