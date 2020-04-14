import sklearn
from sklearn.cluster import KMeans
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class KMeans(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        clusters = conf.get_entry('clusters')  # {“gini”, “entropy”}
        n_clusters = int(conf.get_entry('n_clusters'))
        init = conf.get_entry('init')
        max_iter = conf.get_entry('max_iter')
        self.kmeans = sklearn.cluster.KMeans(n_clusters=n_clusters, init=init, max_iter=max_iter)

    def train(self):
        self.kmeans.fit(self.X)

    def predict(self):
        return self.kmeans.predict(self.X)
