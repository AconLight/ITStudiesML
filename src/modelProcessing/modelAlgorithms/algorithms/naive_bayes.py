import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import check_cv
from sklearn.linear_model import LogisticRegression
from sklearn.base import is_classifier
from sklearn.datasets import load_iris

from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from src.modelProcessing.modelAlgorithms.effectiveness import plot_learning_curve

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class NaiveBayes(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        var_smoothing = float(conf.get_entry('var_smoothing'))
        self.classifier = GaussianNB(var_smoothing=var_smoothing)

    def train(self):
        fig, axes = plt.subplots(3, 2, figsize=(10, 15))

        cv = 5
        estimator = LogisticRegression()
        cv = check_cv(cv, self.Y_train, classifier=is_classifier(estimator))
        cv_iter = list(cv.split(self.X_train, self.Y_train))
        custom_cv = zip(self.X_test, self.Y_test)

        title = "Learning Curves (Naive Bayes)"
        # # Cross validation with 100 iterations to get smoother mean test and train
        # # score curves, each time with 20% data randomly selected as a validation set.
        #
        plot_learning_curve(self.classifier, title, self.X_train, self.Y_train, axes=axes[:, 1], ylim=(0, 1.01),
                            cv=ShuffleSplit(n_splits=100, test_size=0.2, random_state=0), n_jobs=4)
        # self.lc = learning_curve(self.classifier, self.X_train, self.Y_train, cv=None, n_jobs=4,
        #                          train_sizes=np.linspace(.1, 1.0, 5),
        #                          return_times=True)

        plt.show()
        self.classifier.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.classifier.predict(self.X_test)
