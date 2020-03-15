from sklearn.naive_bayes import GaussianNB


class NaiveBayes:
    def __init__(self, conf) -> None:
        super().__init__()
        var_smoothing = float(conf.get_entry('var_smoothing'))
        self.classifier = GaussianNB(var_smoothing=var_smoothing)

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
