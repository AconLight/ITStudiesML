import sys

import pandas

from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType, \
    DataLoadingConfigurationEntries
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
from src.evaluation.evaluationManager import EvaluationManager
from src.modelProcessing.modelProcessor import ModelProcessor
from os.path import sep
from itertools import product
from datetime import datetime

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

best_results = {}

print()

file = open("results" + sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".txt", "w+")

for db in range(len(db_confs)):
    db_conf = parse_add_conf({}, dataLoadingConfigsPath + sep + db_confs[db])
    for m in range(len(model_confs)):
        model_conf = parse_add_conf({}, modelProcessingConfigsPath + sep + model_confs[m])
        model_algorithm = model_conf.pop('modelAlgorithm', None)
        # print(model_conf)
        model_params = []
        model_params_keys = []
        for key in model_conf:
            model_params.append(model_conf[key])
            model_params_keys.append(key)

        model_params_product = product(*model_params)
        # print(list(model_params_product))

        my_model_conf = {'modelAlgorithm': model_algorithm}



        for m in list(model_params_product):
            for k in range(len(model_params_keys)):
                my_model_conf[model_params_keys[k]] = m[k]

            best_results[db_confs[db] + ", " + str(model_algorithm)] = 0
            file.write(str(my_model_conf) + '\n')
            for e in range(len(evaluation_confs)):
                print(my_model_conf)
                evaluation_conf = parse_add_conf({}, evaluationConfigsPath + sep + evaluation_confs[e])
                # creating model (dataLoading - modelProcessing - evaluation)
                dataLoader = CsvDataLoader(Configuration(ConfigurationType.DATALOADING, db_conf), file=file)
                modelProcessor = ModelProcessor(Configuration(ConfigurationType.CLASSIFICATION, my_model_conf), file=file)
                evaluationManager = EvaluationManager(Configuration(ConfigurationType.EVALUATION, evaluation_conf),
                                                      file=file)
                # processing
                data_map = dataLoader.load()
                print("dupa")
                print(data_map.keys())
                process_result = modelProcessor.process(data_map)
                results = evaluationManager.evaluate(process_result, data_map)
                if best_results[db_confs[db] + ", " + str(model_algorithm)] < results[0]:
                    best_results[db_confs[db] + ", " + str(model_algorithm)] = str(my_model_conf) + str(results[0])
                file.write('\n')


file.close()
file2 = open("best_results" + sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".txt", "w+")
for key in best_results:
    file2.write(key + " - " + str(best_results[key]) + "\n")

file2.close()
