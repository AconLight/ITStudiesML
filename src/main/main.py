import sys
from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType
from src.dataLoading.csv_data_loader import CsvDataLoader
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
    modelProcessingConf = parse_add_conf(modelProcessingConf, defaultModelProcessingConfigsPath + sep + runArgs[2])

if runArgsLength > 2:
    evaluationConf = parse_add_conf(evaluationConf, evaluationConfigsPath + sep + runArgs[3])

print(dataLoadingConf)

# creating model (dataLoading - modelProcessing - evaluation)
dataLoader = CsvDataLoader(Configuration(ConfigurationType.DATALOADING, dataLoadingConf))
modelProcessor = ModelProcessor(Configuration(ConfigurationType.CLASSIFICATION, modelProcessingConf))
evaluationManager = EvaluationManager(Configuration(ConfigurationType.EVALUATION, evaluationConf))

X_train, X_test, Y_train, Y_test = dataLoader.load()
classificationOutput = modelProcessor.process(X_train, X_test, Y_train, Y_test)
results = evaluationManager.evaluate(classificationOutput)

results.show()
