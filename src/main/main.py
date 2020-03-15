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

runArgs = sys.argv
runArgsLength = len(runArgs) - 1  # first arg is an execution path, dunno why...

dataLoadingConf = parse_add_conf({}, defaultDataLoadingConfigsPath)
modelProcessingConf = parse_add_conf({}, defaultModelProcessingConfigsPath)
evaluationConf = parse_add_conf({}, defaultEvaluationConfigsPath)

if runArgsLength > 0:
    dataLoadingConf = parse_add_conf(dataLoadingConf, dataLoadingConfigsPath + sep + runArgs[1])

if runArgsLength > 1:
    modelProcessingConf = parse_add_conf(modelProcessingConf, modelProcessingConfigsPath + sep + runArgs[2])

if runArgsLength > 2:
    evaluationConf = parse_add_conf(evaluationConf, evaluationConfigsPath + sep + runArgs[3])

print(dataLoadingConf)

# creating model (dataLoading - modelProcessing - evaluation)
data_loading_configuration = Configuration(ConfigurationType.DATALOADING, dataLoadingConf)
dataLoader = CsvDataLoader(data_loading_configuration)
modelProcessor = ModelProcessor(Configuration(ConfigurationType.CLASSIFICATION, modelProcessingConf))
evaluationManager = EvaluationManager(Configuration(ConfigurationType.EVALUATION, evaluationConf))

dataset = dataLoader.load()
X_train, Y_train, X_test, Y_test = TrainTestSplitter.split(dataset,float(data_loading_configuration.get_entry(DataLoadingConfigurationEntries.TEST_SET_PERCENTAGE.value)))
Y_pred = modelProcessor.process(X_train, X_test, Y_train)
results = evaluationManager.evaluate(Y_pred, Y_test)

results.show()
