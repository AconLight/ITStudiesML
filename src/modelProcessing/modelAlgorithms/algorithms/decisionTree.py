from sklearn.tree import DecisionTreeClassifier


class DecisionTree:
    def __init__(self, conf) -> None:
        super().__init__()
        criterion = conf.get_entry('criterion')  # {“gini”, “entropy”}
        splitter = conf.get_entry('splitter')  # {“best”, “random”}
        max_depth = int(conf.get_entry('max_depth'))
        min_samples_split = int(conf.get_entry('min_samples_split'))
        min_samples_leaf = int(conf.get_entry('min_samples_leaf'))
        self.classifier = DecisionTreeClassifier(criterion=criterion, splitter=splitter, max_depth=max_depth,
                                                 min_samples_split=min_samples_split,
                                                 min_samples_leaf=min_samples_leaf)

        
    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
