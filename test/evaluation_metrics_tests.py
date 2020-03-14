from unittest import TestCase

from src.evaluation.evaluationMetric.confusion_matrix import ConfusionMatrix
from test.data.datasets_object_mother import DatasetsObjectMother


class EvaluationMetricsTest(TestCase):
    def test_create_confusion_matrix_for_single_column_integer_predictions(self):
        #given
        dataset_with_encoded_columns = DatasetsObjectMother.students_dataset_with_encoded_columns
        classified_column = 'Country'
        Y_pred = dataset_with_encoded_columns.get_column('Country')
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


