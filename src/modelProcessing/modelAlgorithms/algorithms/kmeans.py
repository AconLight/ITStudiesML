import sklearn
from sklearn.cluster import KMeans
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class KMeans(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        n_clusters = int(conf.get_entry('n_clusters'))
        init = conf.get_entry('init')
        max_iter = int(conf.get_entry('max_iter'))
        self.model_algorithm = sklearn.cluster.KMeans(n_clusters=n_clusters, init=init, max_iter=max_iter)

    def train(self):
        self.model_algorithm.fit(self.X)

    def predict(self):
        return self.model_algorithm.predict(self.X)
