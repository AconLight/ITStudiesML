from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase
from src.serialization_flow.serialize_service import deserialize_model


def predict(data):
    model_algorithm = deserialize_model('drzewka')

    # preprocess TODO

    return model_algorithm.predict(data)






