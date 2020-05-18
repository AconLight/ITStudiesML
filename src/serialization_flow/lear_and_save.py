from datetime import datetime
from os.path import sep

from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.modelProcessing.modelProcessor import ModelProcessor
from src.serialization_flow.serialize_service import serialize_model, deserialize_model

AdaBoost = "AdaBoost.csv"
XGBoost = "XGBoost.csv"
SVM = "SVM.csv"
RandomForest = "RandomForest.csv"

#############    CHANGE    HERE    ALGORITHM    ###################
algorithm = RandomForest

db_conf_path = "project_learn_and_save_configs" + sep + "database.csv"
model_conf_path = "project_learn_and_save_configs" + sep + algorithm

db_conf = parse_add_conf({}, db_conf_path)
model_conf = parse_add_conf({}, model_conf_path)


file = open("results" + sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".txt", "w+")
dataLoader = CsvDataLoader(Configuration(ConfigurationType.DATALOADING, db_conf), file=file)
modelProcessor = ModelProcessor(Configuration(ConfigurationType.CLASSIFICATION, model_conf), file=file, db_conf=Configuration(ConfigurationType.DATALOADING, db_conf))

# processing
data_map = dataLoader.load()

print(data_map)

process_result = modelProcessor.process(data_map)
model_algorithm = modelProcessor.model.model_algorithm

print(model_algorithm)

serialize_model(model_algorithm, 'drzewka')

m2 = deserialize_model('drzewka')

print(m2)