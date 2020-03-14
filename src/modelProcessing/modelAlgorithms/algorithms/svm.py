from sklearn.svm import SVC

class SVM:
    def __init__(self):
        self.clf = SVC(kernel='linear')
        print("SVM initialized")

    def train(self, X_train, Y_train):
        self.clf.fit(X_train, Y_train)

    def predict(self, X_test):
        y_pred = self.clf.predict(X_test)
        return y_pred