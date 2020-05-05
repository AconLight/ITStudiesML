from sklearn.svm import SVC

import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class SVM(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        self.clf = SVC(
            kernel=conf.get_entry('kernel'),  # ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
            tol=float(conf.get_entry('tol'))  # tolerance error
        )

    def train(self):
        self.clf.fit(self.X_train, self.Y_train)
        self.learning_data = learning_curve(self.clf, self.X_train, self.Y_train,
                                            cv=ShuffleSplit(n_splits=100, test_size=0.2, random_state=0), n_jobs=4,
                                            train_sizes=np.linspace(.1, 1.0, 5),
                                            return_times=True)

    def predict(self):
        y_pred = self.clf.predict(self.X_test)
        return y_pred
