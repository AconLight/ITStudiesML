from sklearn.ensemble import RandomForestClassifier

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class RandomForest(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        self.model_algorithm = RandomForestClassifier(
            n_estimators=int(conf.get_entry('n_estimators')),
            max_depth=int(conf.get_entry('max_depth')),
            max_leaf_nodes=int(conf.get_entry('max_leaf_nodes')),
        )

    def train(self):
        self.model_algorithm.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.model_algorithm.predict(self.X_test)
