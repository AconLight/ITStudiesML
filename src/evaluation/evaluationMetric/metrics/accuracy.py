from src.evaluation.evaluationMetric.confusion_matrix import ConfusionMatrix
import numpy as np

class AccuracyMetric():

    def calculate(self, pd_Y_pred, pd_Y_test):
        confusion_matrix = ConfusionMatrix().calculate(pd_Y_pred, pd_Y_test)

        number_of_examples = np.sum(np.sum(confusion_matrix))
        correctly_classified = np.sum(np.diag(confusion_matrix))

        return correctly_classified/number_of_examples

