from sklearn.ensemble import RandomForestClassifier


class RandomForest:
    def __init__(self, conf) -> None:
        super().__init__()
        self.classifier = RandomForestClassifier(
            n_estimators=int(conf.get_entry('n_estimators')),
            max_depth=int(conf.get_entry('max_depth')),
            max_leaf_nodes=int(conf.get_entry('max_leaf_nodes')),
        )

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
