from sklearn.svm import SVC

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class SVM(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        self.clf = SVC(
            kernel=conf.get_entry('kernel'), # ‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’
            tol=float(conf.get_entry('tol')) # tolerance error
        )

    def train(self):
        self.clf.fit(self.X_train, self.Y_train)

    def predict(self):
        y_pred = self.clf.predict(self.X_test)
        return y_pred