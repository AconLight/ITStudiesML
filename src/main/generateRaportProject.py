import sys

import pandas

from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType, \
    DataLoadingConfigurationEntries
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.dataLoading.preprocessing.train_test_split import TrainTestSplitter
from src.evaluation.evaluationManager import EvaluationManager
from src.evaluation.evaluationMetric.metrics import RocCurve
from src.main.ResultStorage import ResultStorage
from src.modelProcessing.modelProcessor import ModelProcessor
from os.path import sep
from itertools import product
from datetime import datetime

# reading specified configurations
from src.serialization_flow.preprocess_data import DataPreprocessor

dataLoadingConfigsPath = "dataLoadingConfigs"
modelProcessingConfigsPath = "modelProcessingConfigs"
evaluationConfigsPath = "evaluationConfigs"

defaultDataLoadingConfigsPath = "defaultConfig" + sep + "dataLoading_2.csv"
defaultModelProcessingConfigsPath = "defaultConfig" + sep + "modelProcessing_2.csv"
defaultEvaluationConfigsPath = "defaultConfig" + sep + "evaluation_2.csv"

dataLoadingConfs = parse_add_conf({}, defaultDataLoadingConfigsPath)
modelProcessingConfs = parse_add_conf({}, defaultModelProcessingConfigsPath)
evaluationConfs = parse_add_conf({}, defaultEvaluationConfigsPath)

db_confs = dataLoadingConfs['db_confs']
model_confs = modelProcessingConfs['model_confs']
evaluation_confs = evaluationConfs['evaluation_confs']

result_storage = ResultStorage()

print()

file = open("results" + sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".txt", "w+")

dp = DataPreprocessor()

preprocess_functions = dp.get_all_possibilities()
for preprocess_function in preprocess_functions:
    for db in range(len(db_confs)):
        db_conf = parse_add_conf({}, dataLoadingConfigsPath + sep + db_confs[db])
        for m in range(len(model_confs)):
            model_conf = parse_add_conf({}, modelProcessingConfigsPath + sep + model_confs[m])
            model_algorithm = model_conf.pop('modelAlgorithm', None)
            print(model_conf)
            model_params = []
            model_params_keys = []
            for key in model_conf:
                model_params.append(model_conf[key])
                model_params_keys.append(key)

            model_params_product = product(*model_params)
            # print(model_params)

            my_model_conf = {'modelAlgorithm': model_algorithm}



            for m in list(model_params_product):
                for k in range(len(model_params_keys)):
                    my_model_conf[model_params_keys[k]] = m[k]

                file.write(str(my_model_conf) + '\n')
                for e in range(len(evaluation_confs)):
                    evaluation_conf = parse_add_conf({}, evaluationConfigsPath + sep + evaluation_confs[e])
                    # print(my_model_conf)
                    # print(db_conf)
                    # print(evaluation_conf)
                    # print(model_params)
                    # creating model (dataLoading - modelProcessing - evaluation)
                    dataLoader = CsvDataLoader(Configuration(ConfigurationType.DATALOADING, db_conf), file=file)
                    dataLoader.preprocess_functions = preprocess_function
                    modelProcessor = ModelProcessor(Configuration(ConfigurationType.CLASSIFICATION, my_model_conf), file=file, db_conf=Configuration(ConfigurationType.DATALOADING, db_conf))
                    evaluationManager = EvaluationManager(Configuration(ConfigurationType.EVALUATION, evaluation_conf),
                                                          file=file)
                    # processing
                    data_map = dataLoader.load()
                    # print(data_map)
                    process_result = modelProcessor.process(data_map)
                    results = evaluationManager.evaluate(process_result, data_map)
                    preprocess_info = ''
                    for func in preprocess_function:
                        preprocess_info += func['name']
                        preprocess_info += ': '
                        preprocess_info += str(func['params'])
                        preprocess_info += ' _ '

                    print('preprocess_info')
                    print(preprocess_info)
                    result_storage.add_result(db_conf['data_file_path'] + preprocess_info, my_model_conf.copy(), results)
                    # if best_results[db_confs[db] + ", " + str(model_algorithm)] < results[0]:
                    #     best_results[db_confs[db] + ", " + str(model_algorithm)] = str(my_model_conf) + str(results[0])
                    file.write('\n')

            print()

# result_storage.show()
result_storage.generate_graphs()

#Generate ROC Curves
if 'RocCurve' in evaluation_conf['evaluationMetrics']:
    algorithm_points_map = {}

    for key in result_storage.best_results.keys():
        dataset, algorithm, metric = key.split()
        params = result_storage.best_results[key]['params']
        if metric == 'RocCurve':
            for class_id in result_storage.best_results[key]['metric_val'].keys():
                if (dataset, algorithm) not in algorithm_points_map:
                    algorithm_points_map[(dataset, algorithm,class_id, str(params))]= result_storage.best_results[key]['metric_val'][class_id]


    RocCurve.visualize(algorithm_points_map)


file.close()
file2 = open("best_results" + sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".txt", "w+")
for key in result_storage.best_results:
    file2.write(key + " - " + str(result_storage.best_results[key]) + "\n")

file2.close()
