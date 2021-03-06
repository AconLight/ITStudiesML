from unittest import TestCase

from src.evaluation.evaluationMetric.confusion_matrix import ConfusionMatrix
from src.evaluation.evaluationMetric.metrics.accuracy import AccuracyMetric
from test.data.datasets_object_mother import DatasetsObjectMother


class EvaluationMetricsTest(TestCase):
    def test_create_confusion_matrix_for_single_column_integer_predictions(self):
        #given
        dataset_with_encoded_columns = DatasetsObjectMother.students_dataset_with_encoded_columns
        classified_column = 'Country'
        Y_pred = dataset_with_encoded_columns.get_column(classified_column)
        Y_test = Y_pred

        #when
        confusion_matrix = ConfusionMatrix().calculate(Y_pred, Y_test)

        #then
        self.assertEqual(confusion_matrix.shape, (3,3))

    def test_create_confusion_matrix_for_binary_encoded_column(self):
        #given
        dataset_with_encoded_columns = DatasetsObjectMother.students_dataset_with_binarized_country_column
        binarized_classified_columns = ['Australia','India', 'US']
        Y_pred = dataset_with_encoded_columns.get_columns(binarized_classified_columns)
        Y_test = Y_pred

        #when
        confusion_matrix = ConfusionMatrix().calculate(Y_pred, Y_test)

        # then
        self.assertEqual(confusion_matrix.shape, (3, 3))

    def test_create_confusion_matrix_for_single_binary_column(self):
        # given
        dataset_with_encoded_columns = DatasetsObjectMother.students_dataset_with_binarized_country_column
        binarized_classified_column = 'US'
        Y_pred = dataset_with_encoded_columns.get_column(binarized_classified_column)
        Y_test = Y_pred

        #when
        confusion_matrix = ConfusionMatrix().calculate(Y_pred, Y_test)

        #then
        self.assertEqual(confusion_matrix.shape, (2, 2))


    def test_calculate_accuracy_metric(self):
        # given
        dataset_with_encoded_columns = DatasetsObjectMother.students_dataset_with_binarized_country_column
        binarized_classified_column = 'US'
        Y_pred = dataset_with_encoded_columns.get_column(binarized_classified_column)
        Y_test = Y_pred

        # when
        accuracy = AccuracyMetric().calculate(Y_pred, Y_pred)

        #then
        self.assertEqual(accuracy,1)
