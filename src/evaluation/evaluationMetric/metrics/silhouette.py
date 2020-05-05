from sklearn.metrics import silhouette_score

from src.common.configuration.conf import DataLoadingGroupingConfigurationEntries
from src.evaluation.evaluationMetric.metrics import ClusterQualityMetric


class Silhouette(ClusterQualityMetric):

    @staticmethod
    def calculate(y_prediction, data_map):
        return silhouette_score(data_map['FEED_COLUMNS'], y_prediction)
