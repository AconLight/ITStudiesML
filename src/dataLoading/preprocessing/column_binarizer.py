from sklearn import preprocessing


class ColumnBinarizer():
    @staticmethod
    def binarize_column(dataset, column_name):
        label_binarizer = preprocessing.LabelBinarizer()
        binarized_column = label_binarizer.fit_transform(dataset.get_column(column_name))
        return label_binarizer.classes_, binarized_column

    @staticmethod
    def add_binarized_column_to_dataset(dataset, column_name):
        binarized_classes, binarized_column = ColumnBinarizer.binarize_column(dataset, column_name)
        dataset.replace_column(column_name, binarized_classes, binarized_column)