from sklearn.tree import tree
from sklearn.datasets import load_iris


class DecisionTree():
    def __init__(self) -> None:
        super().__init__()
        # criterion =
        # splitter =
        # max_depth =
        # min_samples_split =
        # min_samples_leaf =
        self.classifier = tree.DecisionTreeClassifier(criterion, splitter, max_depth, min_samples_split,
                                                      min_samples_leaf)

    def train(self,X_train, Y_train):
        self.classifier.fit(X_train, Y_train)

    def predict(self,X_test):
        return self.classifier.predict(X_test)