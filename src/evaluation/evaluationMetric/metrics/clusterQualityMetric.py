from sklearn.metrics import accuracy_score, calinski_harabasz_score, davies_bouldin_score

from src.common.configuration.conf import DataLoadingGroupingConfigurationEntries


class ClusterQualityMetric:

    @staticmethod
    def calculate(y_prediction, data_map):
        return 1


