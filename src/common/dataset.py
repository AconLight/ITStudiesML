class Dataset():
    def __init__(self, dataframe) -> None:
        super().__init__()
        self.data = dataframe
        self.target_columns = []
        self.data_columns = []
        self.column_mapping = {}
        for column in self.data.columns:
            self.column_mapping[column] = [column]

    # def get_string_columns(self):
    #     # (df.applymap(type) == str).all(0)
    #     return self.data.select_dtypes(include='object').columns

    def get_columns(self, column_name_list):
        self.check_if_columns_are_in_data(column_name_list)
        return self.data.filter(items=column_name_list)

    def set_target_columns(self, column_name_list):
        self.check_if_columns_are_in_data(column_name_list)
        self.target_columns = column_name_list

    def check_if_columns_are_in_data(self, column_name_list):
        illegal_column_names = [column_name for column_name in column_name_list if
                                column_name not in self.column_mapping.keys()]
        if len(illegal_column_names) > 0:
            raise ValueError("Trying to set column(s) which does not occur in dataset: " + ','.join(
                illegal_column_names))

    def set_data_columns(self, column_name_list):
        self.check_if_columns_are_in_data(column_name_list)
        self.check_if_columns_are_not_target(column_name_list)
        self.data_columns = column_name_list

    def check_if_columns_are_not_target(self, column_name_list):
        illegal_columns = set(column_name_list).intersection(self.target_columns)
        if len(illegal_columns) > 0:
            raise ValueError("Trying to set columns that are marked as target ones: " + ','.join(illegal_columns))

    def get_data_columns(self):
        return self.data_columns

    def get_target_columns(self):
        return self.target_columns

    def drop_column(self, column_name):
        self.check_if_column_is_in_not_data_columns(column_name)
        del self.column_mapping[column_name]
        self.data = self.data.drop(column_name, 1)

    def check_if_column_is_in_not_data_columns(self, column_name):
        if not self.is_column_in_data(column_name):
            raise ValueError("Column which doesn't exist \"" + column_name + "\"")

    def add_column(self, column_name, values):
        self.check_if_column_is_in_data_columns(column_name)
        self.column_mapping[column_name] = column_name
        self.data[column_name] = values

    def check_if_column_is_in_data_columns(self, column_name):
        if self.is_column_in_data(column_name):
            raise ValueError("Column already exists \"" + column_name + "\"")

    def is_column_in_data(self, column_name):
        return column_name in self.column_mapping.keys()

