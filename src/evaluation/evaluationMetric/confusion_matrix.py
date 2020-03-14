import numpy as np


class ConfusionMatrix:
    def __init__(self) -> None:
        super().__init__()

    def calculate(self, pd_Y_pred, pd_Y_test):
        Y_pred = pd_Y_pred.to_numpy()
        Y_test = pd_Y_test.to_numpy()


        # if not np.any(Y_test in (0,1)) and Y_pred.shape[1] == 1:
        #     #Case 1 -> Binary single label
        #

        if np.any(Y_test > 1.0):
            # Case 1 -> Non-binary - Multiclass single integer column
            number_of_class_index = np.max(Y_pred)+1
            self.confusion_matrix = np.zeros((number_of_class_index, number_of_class_index), dtype=np.int32)

            for i in range(Y_pred.shape[0]):
                predicted_class = Y_pred[i]
                actual_class = Y_test[i]
                self.confusion_matrix[predicted_class, actual_class] += 1

        else:
            # Case 2 -> Binary - Multiclass class binary (can be divided into case 3 multilabel)
            # TODO -> single binary variable case
            # TODO -> multilabel case
            number_of_class_index = Y_pred.shape[1]
            self.confusion_matrix = np.zeros((number_of_class_index, number_of_class_index), dtype=np.int32)

            for i in range(Y_pred.shape[0]):
                predicted_class = np.argmax(Y_pred[i])
                actual_class = np.argmax(Y_test[i])
                self.confusion_matrix[predicted_class, actual_class] += 1

        return self.confusion_matrix

    def get_value(self):
        return self.confusion_matrix

    def get_message(self):
        pass