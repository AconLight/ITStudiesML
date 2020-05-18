from src.serialization_flow.preprocess_algorithms.algorithms.ZScore import ZScore


class DataPreprocessor():

    def __init__(self):
        self.data_preprocess_elements = [ZScore()]

    def load(self):
        pass

    def save(self):
        pass

    def preprocess(self, data):
        for data_preprocess_element in self.data_preprocess_elements:
            pass
            # data = data_preprocess_element(data)

        return data

    def run_all_possibilities(self, data):
        for data_preprocess_element in self.data_preprocess_elements:
            for function in data_preprocess_element.get_all_params_possibilities():
                function(data)
