from sklearn import preprocessing


class ColumnEncoder():
    @staticmethod
    def encode_column(dataset, column_name):
        label_encoder = preprocessing.LabelEncoder()
        binarized_column = label_encoder.fit_transform(dataset.get_column(column_name))
        return label_encoder.classes_, binarized_column

    @staticmethod
    def add_binarized_column_to_dataset(dataset, column_name):
        encoded_classes, encoded_column = ColumnEncoder.encode_column(dataset, column_name)
        dataset.replace_column(column_name, column_name, [encoded_column])