import sys

import pandas

from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType, \
    DataLoadingConfigurationEntries
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
from src.evaluation.evaluationManager import EvaluationManager
from src.modelProcessing.modelProcessor import ModelProcessor
from os.path import sep

# reading specified configurations
dataLoadingConfigsPath = "dataLoadingConfigs"
modelProcessingConfigsPath = "modelProcessingConfigs"
evaluationConfigsPath = "evaluationConfigs"

defaultDataLoadingConfigsPath = "defaultConfig" + sep + "dataLoading.csv"
defaultModelProcessingConfigsPath = "defaultConfig" + sep + "modelProcessing.csv"
defaultEvaluationConfigsPath = "defaultConfig" + sep + "evaluation.csv"

dataLoadingConfs = parse_add_conf({}, defaultDataLoadingConfigsPath)
modelProcessingConfs = parse_add_conf({}, defaultModelProcessingConfigsPath)
evaluationConfs = parse_add_conf({}, defaultEvaluationConfigsPath)

db_confs = dataLoadingConfs['db_confs']
model_confs = modelProcessingConfs['model_confs']
evaluation_confs = evaluationConfs['evaluation_confs']

for db in range(len(db_confs)):
    db_conf = parse_add_conf({}, dataLoadingConfigsPath + sep + db_confs[db])
    for m in range(len(model_confs)):
        model_conf = parse_add_conf({}, modelProcessingConfigsPath + sep + model_confs[m])
        for e in range(len(evaluation_confs)):
            evaluation_conf = parse_add_conf({}, evaluationConfigsPath + sep + evaluation_confs[e])
            # creating model (dataLoading - modelProcessing - evaluation)
            dataLoader = CsvDataLoader(Configuration(ConfigurationType.DATALOADING, db_conf))
            modelProcessor = ModelProcessor(Configuration(ConfigurationType.CLASSIFICATION, model_conf))
            evaluationManager = EvaluationManager(Configuration(ConfigurationType.EVALUATION, evaluation_conf))
            # processing
            dataset = dataLoader.load()
            X_train, Y_train, X_test, Y_test = TrainTestSplitter.split(dataset, float(
                db_conf[DataLoadingConfigurationEntries.TEST_SET_PERCENTAGE.value]))
            Y_pred = modelProcessor.process(X_train, X_test, Y_train)
            results = evaluationManager.evaluate(Y_pred, Y_test)
            results.show()
            print()






