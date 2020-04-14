from sklearn.naive_bayes import GaussianNB

from src.modelProcessing.modelAlgorithms.algorithmBase import AlgorithmBase


class NaiveBayes(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        var_smoothing = float(conf.get_entry('var_smoothing'))
        self.classifier = GaussianNB(var_smoothing=var_smoothing)

    def train(self):
        self.classifier.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.classifier.predict(self.X_test)
