from src.modelProcessing.modelAlgorithms.algorithmBaseClassification import AlgorithmBase
from src.serialization_flow.serialize_service import deserialize_model

#expected columns: ['meanfreq', 'sd', 'median', 'Q25', 'IQR', 'skew', 'kurt', 'sp.ent', 'sfm', 'mode', 'centroid', 'meanfun', 'minfun', 'maxfun', 'meandom', 'mindom', 'maxdom', 'dfrange', 'modindx']
def predict(data):
    model_algorithm = deserialize_model('drzewka')
    return model_algorithm.predict(data)






