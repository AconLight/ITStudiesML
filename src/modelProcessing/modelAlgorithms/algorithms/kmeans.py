import sklearn
from sklearn.cluster import KMeans
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class KMeans(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        self.kmeans = sklearn.cluster.KMeans()

    def train(self):
        self.kmeans.fit(self.X)

    def predict(self):
        return self.kmeans.predict(self.X)