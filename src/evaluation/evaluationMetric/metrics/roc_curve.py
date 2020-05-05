import os
from datetime import datetime

from sklearn.metrics import roc_curve, roc_auc_score, auc
import matplotlib.pyplot as plt
import numpy as np

class RocCurve:

    @staticmethod
    def calculate(y_prediction, data_map):
        return RocCurve.roc_auc_score_multiclass(data_map["CLASSIFICATION_COLUMN_test"], y_prediction)

    @staticmethod
    def roc_auc_score_multiclass(actual_class, pred_class, average="macro"):
        # creating a set of all the unique classes using the actual class list
        unique_class = set([x[0] for x in actual_class.values.tolist()])
        roc_auc_dict = {}
        for per_class in unique_class:
            # creating a list of all the classes except the current class
            other_class = [x for x in unique_class if x != per_class]

            # marking the current class as 1 and all other classes as 0
            new_actual_class = [0 if x[0] in other_class else 1 for x in actual_class.values.tolist()]
            new_pred_class = [0 if x[0] in other_class else 1 for x in pred_class.values.tolist()]

            # class_percentage = len([x for x in len(new_actual_class) if x == 1])/len(actual_class)

            # using the sklearn metrics method to calculate the roc_auc_score
            # roc_auc = roc_auc_score(new_actual_class, new_pred_class, average=average)

            fpr, tpr, _ = roc_curve(new_actual_class, new_pred_class)
            roc_auc = auc(fpr, tpr)

            roc_auc_dict[per_class] = (fpr,tpr,roc_auc)

        return roc_auc_dict

    @staticmethod
    def visualize(algorithm_roc_points_map):

        dataset_class_map = {}

        for key in algorithm_roc_points_map.keys():
            dataset, algorithm, class_id, params = key
            dc_key = (dataset, class_id)
            if dc_key not in dataset_class_map.keys():
                dataset_class_map[dc_key] = []

            # dataset_class_map[dc_key].append((algorithm + ' ' + params, algorithm_roc_points_map[key]))
            dataset_class_map[dc_key].append((algorithm, algorithm_roc_points_map[key]))

        for key in dataset_class_map.keys():
            dataset,class_id = key

            title = dataset + " " + " class " + str(class_id)
            for ar_entry in dataset_class_map[key]:
                algorithm_label, points = ar_entry
                fpr,tpr,roc_auc = points
                plt.plot(fpr, tpr,  label= algorithm_label)

            plt.legend()

            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title(title)
            plt.legend(loc="lower right")
            plt.savefig('results' + os.sep + 'roc_curves' + os.sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + title.replace('/', '-').replace(' ','') +'.png')
            plt.savefig('results' + os.sep + 'test.png')
            plt.clf()