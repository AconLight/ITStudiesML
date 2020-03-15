from sklearn.tree import DecisionTreeClassifier

class DecisionTree():
    def __init__(self, conf) -> None:
        super().__init__()
        criterion = conf.get_entry('criterion')
        splitter = conf.get_entry('splitter')
        max_depth = int(conf.get_entry('max_depth'))
        min_samples_split = int(conf.get_entry('min_samples_split'))
        min_samples_leaf = int(conf.get_entry('min_samples_leaf'))
        self.classifier = DecisionTreeClassifier(criterion, splitter, max_depth, min_samples_split,
                                                      min_samples_leaf)

    def train(self,X_train, Y_train):
        self.classifier.fit(X_train, Y_train)

    def predict(self,X_test):
        return self.classifier.predict(X_test)