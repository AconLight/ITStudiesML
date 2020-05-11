import sklearn
from sklearn.cluster import DBSCAN
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup


class DBSCAN(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        self.min_samples = int(conf.get_entry('min_samples'))
        self.eps = float(conf.get_entry('eps'))
        self.algorithm = conf.get_entry('algorithm')

    def train(self):
        model_algorithm = sklearn.cluster.DBSCAN(min_samples=self.min_samples, eps=self.eps, algorithm=self.algorithm)
        self.dbpred = None
        self.dbpred = model_algorithm.fit_predict(self.X)

    def predict(self):
        return self.dbpred