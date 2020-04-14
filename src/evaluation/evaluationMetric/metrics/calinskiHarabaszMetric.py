from sklearn.metrics import calinski_harabasz_score

from src.common.configuration.conf import DataLoadingGroupingConfigurationEntries
from src.evaluation.evaluationMetric.metrics import ClusterQualityMetric


class CalinskiHarabaszMetric(ClusterQualityMetric):

    @staticmethod
    def calculate(y_prediction, data_map):
        return calinski_harabasz_score(data_map['FEED_COLUMNS'], y_prediction)
