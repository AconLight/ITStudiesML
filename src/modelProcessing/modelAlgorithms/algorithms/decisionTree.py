from sklearn.tree import tree
from sklearn.datasets import load_iris


class DecisionTree():
    def __init__(self, criterion, splitter, max_depth, min_samples_split, min_samples_leaf) -> None:
        super().__init__()
        self.classifier = tree.DecisionTreeClassifier(criterion, splitter, max_depth, min_samples_split,
                                                      min_samples_leaf)

    def train(self,X_train, Y_train):
        self.classifier.fit(X_train, Y_train)

    def predict(self,X_test):
        return self.classifier.predict(X_test)