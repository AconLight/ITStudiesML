

class DataLoader:
    def __init__(self, configuration):
        self.feedColumns = configuration.get_entry('feedColumns')
        self.classificationColumn = configuration.get_entry('classificationColumn')
        self.data_file_path = configuration.get_entry('data_file_path')


    def load(self, encoding="ISO-8859-1"):
        pass
