from sklearn.neural_network import MLPClassifier


class MLP:
    def __init__(self, conf) -> None:
        super().__init__()
        alpha = float(conf.get_entry('alpha'))
        hidden_layer_count = int(conf.get_entry('hidden_layer_count'))
        hidden_layer_neurons = int(conf.get_entry('hidden_layer_neurons'))
        hidden_layer_sizes = (hidden_layer_neurons,hidden_layer_count)
        solver = conf.get_entry('solver')
        self.classifier = MLPClassifier(alpha=alpha, hidden_layer_sizes=hidden_layer_sizes, solver=solver)

    def train(self, x_train, y_train):
        self.classifier.fit(x_train, y_train)

    def predict(self, x_test):
        return self.classifier.predict(x_test)
