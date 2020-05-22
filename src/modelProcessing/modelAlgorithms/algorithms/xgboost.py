
# from xgboost import XGBClassifier
from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class XGBoost(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        # max_depth = int(conf.get_entry('max_depth'))
        # sampling_method = conf.get_entry('sampling_method')  # {uniform, gradient_based}
        # num_parallel_tree = int(conf.get_entry('num_parallel_tree'))
        # self.model_algorithm = XGBClassifier(max_depth=max_depth, sampling_method=sampling_method, num_parallel_tree=num_parallel_tree)

    def train(self):
        pass
        # self.model_algorithm.fit(self.X_train, self.Y_train)

    def predict(self):
        pass
        # return self.model_algorithm.predict(self.X_test)

