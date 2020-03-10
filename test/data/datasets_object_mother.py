import pandas as pd

from src.common.dataset import Dataset


class DatasetsObjectMother():
    students_dataset = Dataset(pd.DataFrame([('jack', 34, 'Sydeny', 'Australia'),
                                             ('Riti', 30, 'Delhi', 'India'),
                                             ('Vikas', 31, 'Mumbai', 'India'),
                                             ('Neelu', 32, 'Bangalore', 'India'),
                                             ('John', 16, 'New York', 'US'),
                                             ('Mike', 17, 'las vegas', 'US')],
                                            columns=['Name', 'Age', 'City', 'Country']))