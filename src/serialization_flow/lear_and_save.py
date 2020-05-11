from datetime import datetime
from os.path import sep

from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.modelProcessing.modelProcessor import ModelProcessor

AdaBoost = "AdaBoost.csv"
XGBoost = "XGBoost.csv"
SVM = "SVM.csv"
RandomForest = "RandomForest.csv"

#############    CHANGE    HERE    ALGORITHM    ###################
algorithm = SVM

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
print(process_result)


