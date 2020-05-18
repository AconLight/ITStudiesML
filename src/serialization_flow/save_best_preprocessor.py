import time
from datetime import datetime
from os.path import sep

from sklearn.metrics import accuracy_score

from src.common.configuration.conf import parse_add_conf, Configuration, ConfigurationType
from src.dataLoading.csv_data_loader import CsvDataLoader
from src.serialization_flow.learnt_model_service import predict
from src.serialization_flow.preprocess_data import DataPreprocessor


# WIP more retardness required
def retarded_score(test_Y, pred_Y, time):
    w1 = 10
    w2 = 100
    return w1 * accuracy_score(test_Y, pred_Y) / (w1 + time*w2)

#     THIS IS TEMP - WRONG DATABASE, WRONG SPLIT (should be 100% test)
def get_data():
    db_conf_path = "project_learn_and_save_configs" + sep + "database.csv"
    db_conf = parse_add_conf({}, db_conf_path)
    file = open("results" + sep + datetime.now().strftime("%Y-%m-%dT%H-%M-%S") + ".txt", "w+")
    dataLoader = CsvDataLoader(Configuration(ConfigurationType.DATALOADING, db_conf), file=file)
    data_map = dataLoader.load()
    test_X = data_map['FEED_COLUMNS_train']
    test_Y = data_map['CLASSIFICATION_COLUMN_train']
    return test_X, test_Y


def save_best_preprocessor():
    test_X, test_Y = get_data()
    best_score = None
    scores = []
    dp = DataPreprocessor()
    for functions in dp.get_all_possibilities():
        result_X = test_X.copy()
        info = []
        ts = time.time()
        for function in functions:
            result_X = function['func'](result_X)
            info.append({'name': function['name'], 'params': function['params']})
        dt = time.time() - ts
        pred_Y = predict(result_X)
        score = {'score': retarded_score(test_Y, pred_Y, dt), 'info': info}
        if best_score is None:
            best_score = score
        elif best_score['score'] < score['score']:
            best_score = score
        scores.append(score)



    print('all scores:')
    print(scores)

    print('best_score')
    print(best_score)

save_best_preprocessor()

