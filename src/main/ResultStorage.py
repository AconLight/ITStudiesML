

class ResultStorage:

    def __init__(self):
        self.all_results = {}
        self.best_results = {}
        self.best_results_by_param = {}
        self.databases = []
        self.algorithms = []
        self.algorithm_params_keys = {}
        self.algorithm_params_keys_values = {}
        self.metrics = []

    def add_result(self, database, model, results):
        algorithm = model.pop('modelAlgorithm')
        params = model
        if database not in self.databases:
            self.databases.append(database)
        if algorithm not in self.algorithms:
            self.algorithms.append(algorithm)
        if algorithm not in self.algorithm_params_keys_values:
            self.algorithm_params_keys_values[algorithm] = {}
            self.algorithm_params_keys[algorithm] = list(params.keys())
        for param_key in params.keys():
            if param_key not in self.algorithm_params_keys_values[algorithm]:
                self.algorithm_params_keys_values[algorithm][param_key] = {}
            self.algorithm_params_keys_values[algorithm][param_key][params[param_key]] = True



        for result in results:
            if str(result['metric']) not in self.metrics:
                self.metrics.append(str(result['metric']))
            key = database + " " + algorithm + " " + str(params) + " " + str(result['metric'])
            self.all_results[key] = result['val']

            keyNoParams = database + " " + algorithm + " " + str(result['metric'])
            if keyNoParams not in self.best_results:
                self.best_results[keyNoParams] = {'params': params, 'metric_val': result['val']}
            else:
                if self.best_results[keyNoParams]['metric_val'] < result['val']:
                    self.best_results[keyNoParams] = {'params': params, 'metric_val': result['val']}



    def get_best_result(self, database, algorithm, metric):
        return self.best_results[database + " " + algorithm + " " + metric]

    def get_best_results_by_param(self, database, algorithm, metric, param):
        local_best = self.best_results[database + " " + algorithm + " " + metric]
        local_best_params = local_best['params']
        results = []
        for value in self.algorithm_params_keys_values[algorithm][param].keys():
            local_best_params[param] = value
            key = database + " " + algorithm + " " + str(local_best_params) + " " + metric
            results.append({'param_val': value, 'metric_val': self.all_results[key]})
        return results

    def show(self):
        print('params')
        print(self.databases)
        print(self.algorithms)
        print(self.algorithm_params_keys)
        print(self.algorithm_params_keys_values)
        print(self.metrics)
        print('all')
        print(self.all_results)
        print('best')
        print(self.best_results)
        print('best by')
        print(self.algorithm_params_keys[self.algorithms[0]][0])
        print(self.get_best_results_by_param(self.databases[0], self.algorithms[0], self.metrics[0], self.algorithm_params_keys[self.algorithms[0]][0]))