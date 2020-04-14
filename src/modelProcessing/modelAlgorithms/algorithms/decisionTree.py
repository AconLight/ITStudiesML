from sklearn.tree import DecisionTreeClassifier

from src.modelProcessing.modelAlgorithms.algorithmBase import AlgorithmBase


class DecisionTree(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        criterion = conf.get_entry('criterion')  # {“gini”, “entropy”}
        splitter = conf.get_entry('splitter')  # {“best”, “random”}
        max_depth = int(conf.get_entry('max_depth'))
        min_samples_split = int(conf.get_entry('min_samples_split'))
        min_samples_leaf = int(conf.get_entry('min_samples_leaf'))
        self.classifier = DecisionTreeClassifier(criterion=criterion, splitter=splitter, max_depth=max_depth,
                                                 min_samples_split=min_samples_split,
                                                 min_samples_leaf=min_samples_leaf)

    def train(self):
        self.classifier.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.classifier.predict(self.X_test)
