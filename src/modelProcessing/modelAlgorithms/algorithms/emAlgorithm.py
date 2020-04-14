import sklearn
from sklearn.mixture import GaussianMixture
from src.modelProcessing.modelAlgorithms.algorithmBaseGroup import AlgorithmBaseGroup

class EMAlgorithm(AlgorithmBaseGroup):
    def __init__(self, conf):
        super().__init__(conf)
        n_components = int(conf.get_entry('n_components'))  # {2, 4, 10}
        n_init = int(conf.get_entry('n_init'))  # {2, 5, 10}
        max_iter = int(conf.get_entry('max_iter'))  # {10, 50, 100}
        init_params = conf.get_entry('init_params')  # {"kmeans", "random"}
        self.gauassianMixture = GaussianMixture(n_components=n_components, n_init=n_init, max_iter=max_iter, init_params=init_params)

    def train(self):
        self.gauassianMixture.fit(self.X)

    def predict(self):
        return self.gauassianMixture.predict(self.X)
