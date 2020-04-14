import sklearn
from sklearn.cluster import DBSCAN
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class DBSCAN(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        self.min_samples = int(conf.get_entry('min_samples'))
        self.leaf_size = int(conf.get_entry('leaf_size'))
        self.algorithm = conf.get_entry('algorithm')

    def train(self):
        dbscan = sklearn.cluster.DBSCAN(min_samples=self.min_samples, leaf_size=self.leaf_size, algorithm=self.algorithm)
        self.dbpred = None
        self.dbpred = dbscan.fit_predict(self.X)

    def predict(self):
        return self.dbpred