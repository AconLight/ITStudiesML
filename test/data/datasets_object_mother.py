import os

import pandas as pd

from src.common.configuration.conf import ConfigurationType, Configuration, DataLoadingConfigurationEntries
from src.common.dataset import Dataset


class DatasetsObjectMother():
    students_dataset = Dataset(pd.DataFrame([('jack', 34, 'Sydeny', 'Australia'),
                                             ('Riti', 30, 'Delhi', 'India'),
                                             ('Neelu', 32, 'Bangalore', 'India'),
                                             ('John', 16, 'New York', 'US'),
                                             ('Mike', 17, 'las vegas', 'US'),
                                             ('Joshua', 22, 'las vegas', 'US')],
                                            columns=['Name', 'Age', 'City', 'Country']))

    students_dataset_with_encoded_columns = Dataset(pd.DataFrame([('jack', 34, 0, 0),
                                                                  ('Riti', 30, 1, 1),
                                                                  ('Neelu', 32, 2, 1),
                                                                  ('John', 16, '3', 2),
                                                                  ('Mike', 17, 4, 2),
                                                                  ('Joshua', 22, 4, 2)],
                                                                 columns=['Name', 'Age', 'City', 'Country']))

    students_dataset_with_binarized_country_column = Dataset(pd.DataFrame([('jack', 34, 'Sydeny', 1, 0, 0),
                                                                           ('Riti', 30, 'Delhi', 0, 1, 0),
                                                                           ('Neelu', 32, 'Bangalore', 0, 1, 0),
                                                                           ('John', 16, 'New York', 0, 0, 1),
                                                                           ('Mike', 17, 'las vegas', 0, 0, 1),
                                                                           ('Joshua', 22, 'las vegas', 0, 0, 1)],
                                                                          columns=['Name', 'Age', 'City', 'Australia',
                                                                                   'India', 'US']))

    speed_dating_csv_configuration = Configuration(
        ConfigurationType.DATALOADING,
        {
            DataLoadingConfigurationEntries.FEED_COLUMNS.value: ['gender', 'order', 'partner', 'samerace', 'age_o',
                                                                 'race_o'],
            DataLoadingConfigurationEntries.CLASSIFICATION_COLUMN.value: 'match',
            DataLoadingConfigurationEntries.DATA_FILEPATH.value: 'test/data/Speed-Dating-Data.csv'.replace('/', os.sep),
            DataLoadingConfigurationEntries.TEST_SET_PERCENTAGE.value: 15,
        }
    )
