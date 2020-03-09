import sys
from src.common.conf import parseAddConf
from src.dataLoading.dataLoader import DataLoader
from src.evaluation.evaluationManager import EvaluationManager
from src.modelProcessing.modelProcessor import ModelProcessor

# reading specified configurations
dataLoadingConfigsPath = "dataLoadingConfigs"
modelProcessingConfigsPath = "modelProcessingConfigs"
evaluationConfigsPath = "evaluationConfigs"

defaultDataLoadingConfigsPath = "defaultConfig/dataLoading.csv"
defaultModelProcessingConfigsPath = "defaultConfig/modelProcessing.csv"
defaultEvaluationConfigsPath = "defaultConfig/evaluation.csv"

runArgs = sys.argv
runArgsLength = len(runArgs) - 1 # first arg is an execution path, dunno why...

dataLoadingConf = parseAddConf({}, defaultDataLoadingConfigsPath)
modelProcessingConf = parseAddConf({}, defaultModelProcessingConfigsPath)
evaluationConf = parseAddConf({}, defaultEvaluationConfigsPath)

if runArgsLength > 0:
    dataLoadingConf = parseAddConf(dataLoadingConf, dataLoadingConfigsPath + "/" + runArgs[1])

if runArgsLength > 1:
    modelProcessingConf = parseAddConf(modelProcessingConf, defaultModelProcessingConfigsPath + "/" + runArgs[2])

if runArgsLength > 2:
    evaluationConf = parseAddConf(evaluationConf, evaluationConfigsPath + "/" + runArgs[3])

print(dataLoadingConf)

# creating model (dataLoading - modelProcessing - evaluation)
dataLoader = DataLoader(dataLoadingConf)
modelProcessor = ModelProcessor(modelProcessingConf)
evaluationManager = EvaluationManager(evaluationConf)

dataSet = dataLoader.load()
classificationOutput = modelProcessor.process(dataSet)
results = evaluationManager.evaluate(classificationOutput)

results.show()



