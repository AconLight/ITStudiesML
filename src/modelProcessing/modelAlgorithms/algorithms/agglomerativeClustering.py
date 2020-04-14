import sklearn
from sklearn.cluster import AgglomerativeClustering
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class AgglomerativeClustering(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        n_clusters = int(conf.get_entry('n_clusters'))  # {2, 4, 10}
        affinity = conf.get_entry('affinity')  # {"euclidean", "l1", "l2", "manhattan", "cosine"}
        linkage = conf.get_entry('linkage')  # {"ward", "complete", "average", "single"}
        self.agglomerativeClustering=AgglomerativeClustering(n_clusters=n_clusters, affinity=affinity, linkage=linkage)

    def train(self):
        self.agglomerativeClustering.fit(self.X)

    def predict(self):
        return self.agglomerativeClustering.fit_predict(self.X)
