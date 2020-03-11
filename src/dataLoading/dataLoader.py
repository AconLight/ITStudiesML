

class DataLoader:
    def __init__(self, configuration):
        # self.feedColumns = conf['feedColumns']
        # self.classificationColumn = conf['classificationColumn']
        self.data_file_path = configuration.get_entry('data_file_path')


    def load(self, encoding="ISO-8859-1"):
        pass
