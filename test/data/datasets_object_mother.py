import os

import pandas as pd

from src.common.configuration.conf import ConfigurationType, Configuration, DataLoadingConfigurationEntries
from src.common.dataset import Dataset


class DatasetsObjectMother():
    students_dataset = Dataset(pd.DataFrame([('jack', 34, 'Sydeny', 'Australia'),
                                             ('Riti', 30, 'Delhi', 'India'),
                                             ('Vikas', 31, 'Mumbai', 'India'),
                                             ('Neelu', 32, 'Bangalore', 'India'),
                                             ('John', 16, 'New York', 'US'),
                                             ('Mike', 17, 'las vegas', 'US')],
                                            columns=['Name', 'Age', 'City', 'Country']))

    speed_dating_csv_configuration = Configuration(
        ConfigurationType.DATALOADING,
        {
            DataLoadingConfigurationEntries.FEED_COLUMNS : ['gender','order','partner','samerace','age_o','race_o'],
            DataLoadingConfigurationEntries.CLASSIFICATION_COLUMN: 'match',
            DataLoadingConfigurationEntries.DATA_FILEPATH: 'test/data/Speed-Dating-Data.csv'.replace('/', os.sep),
        }
    )