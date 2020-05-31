from itertools import product

class PreprocessAlgorithmBase():

    columns_numb = 4

    def __init__(self):
        self.params_possibilities = {}
        self.name = 'base'

    def preprocess(self, data, y, params):
        return data


    def get_all_params_possibilities(self):
        preprocess_functions = []
        my_params = []
        for key in self.params_possibilities.keys():
            one_param_possibilities = self.params_possibilities[key]
            one_param_possibilities_with_keys = []
            for param in one_param_possibilities:
                one_param_possibilities_with_keys.append({key: param})
            my_params.append(one_param_possibilities_with_keys)

        all_params_possibilities = list(product(*my_params))
        print('all_params_possibilities')
        print(all_params_possibilities)
        self.params_possibility_dic_list = []
        idx = 0
        for params_possibility in all_params_possibilities:
            self.params_possibility_dic_list.append({})
            for param in params_possibility:
                self.params_possibility_dic_list[idx][list(param.keys())[0]] = param[list(param.keys())[0]]

            print('params_possibility_dic')
            print(self.params_possibility_dic_list[idx])
            preprocess_functions.append({'name': self.name, 'params': self.params_possibility_dic_list[idx], 'func': lambda data, y, my_idx=idx: self.preprocess(data, y, self.params_possibility_dic_list[my_idx])})
            idx += 1
        return preprocess_functions
