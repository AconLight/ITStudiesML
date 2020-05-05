from sklearn.metrics import davies_bouldin_score

from src.common.configuration.conf import DataLoadingGroupingConfigurationEntries
from src.evaluation.evaluationMetric.metrics import ClusterQualityMetric


class DaviesBouldin(ClusterQualityMetric):

    @staticmethod
    def calculate(y_prediction, data_map):
        return davies_bouldin_score(data_map['FEED_COLUMNS'], y_prediction)
