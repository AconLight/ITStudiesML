import copy
from unittest import TestCase

from src.dataLoading.preprocessing.column_binarizer import ColumnBinarizer
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

    def test_binarize_country_column(self):
        #given
        dataset = copy.deepcopy(DatasetsObjectMother.students_dataset)
        binarized_column_name = 'Country'
        column_binarizer = ColumnBinarizer()

        #when
        classes, columns = column_binarizer.binarize_column(dataset,binarized_column_name)

        #then
        self.assertEqual(len(classes), 3)

    def test_adding_binarized_country_to_dataset(self):
        #given
        dataset = copy.deepcopy(DatasetsObjectMother.students_dataset)
        binarized_column_name = 'Country'
        column_binarizer = ColumnBinarizer()

        #when
        number_of_columns_before_replacement = dataset.get_number_of_columns()
        column_binarizer.add_binarized_column_to_dataset(dataset, binarized_column_name)

        #then
        number_of_columns_after_replacement = dataset.get_number_of_columns()
        self.assertEqual( number_of_columns_after_replacement - number_of_columns_before_replacement, 2 )