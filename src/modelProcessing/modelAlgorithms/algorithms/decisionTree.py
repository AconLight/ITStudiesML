from sklearn.tree import DecisionTreeClassifier

import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


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
        self.learning_data = learning_curve(self.classifier, self.X_train, self.Y_train,
                                            cv=ShuffleSplit(n_splits=100, test_size=0.2, random_state=0), n_jobs=4,
                                            train_sizes=np.linspace(.1, 1.0, 5),
                                            return_times=True)

    def predict(self):
        return self.classifier.predict(self.X_test)
