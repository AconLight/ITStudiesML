from sklearn.neural_network import MLPClassifier

from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase


class MLP(AlgorithmBase):
    def __init__(self, conf):
        super().__init__(conf)
        alpha = float(conf.get_entry('alpha'))
        hidden_layer_count = int(conf.get_entry('hidden_layer_count'))
        hidden_layer_neurons = int(conf.get_entry('hidden_layer_neurons'))
        hidden_layer_sizes = (hidden_layer_neurons,hidden_layer_count)
        solver = conf.get_entry('solver')
        self.classifier = MLPClassifier(alpha=alpha, hidden_layer_sizes=hidden_layer_sizes, solver=solver)

    def train(self):
        self.classifier.fit(self.X_train, self.Y_train)

    def predict(self):
        return self.classifier.predict(self.X_test)
