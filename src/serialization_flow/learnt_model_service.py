from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase
from src.serialization_flow.serialize_service import deserialize_model

#expected columns: minfun dfrange modindx sp.ent sfm mode meandom mindom maxdom Q25 sd meanfreq centroid median IQR Q75 skew
def predict(data):
    model_algorithm = deserialize_model('drzewka')
    return model_algorithm.predict(data)






