from unittest import TestCase

import pandas as pd
import copy

from numpy import NaN

from src.common.dataset import Dataset


class DatasetTests(TestCase):
    students_dataset = Dataset(pd.DataFrame([('jack', 34, 'Sydeny', 'Australia'),
                                             ('Riti', 30, 'Delhi', 'India'),
                                             ('Vikas', 31, 'Mumbai', 'India'),
                                             ('Neelu', 32, 'Bangalore', 'India'),
                                             ('John', 16, 'New York', 'US'),
                                             ('Mike', 17, 'las vegas', 'US')],
                                            columns=['Name', 'Age', 'City', 'Country']))

    def test_should_add_new_column(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        new_column_name = "new_column"
        new_column_values = [5, NaN, NaN, 10, 1, 7]

        # when
        dataset.add_column(new_column_name, new_column_values)
        # print(dataset.data.head())

        # then
        self.assertTrue(dataset.is_column_in_data(new_column_name))

    def test_not_allow_to_add_existing_column(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        column_name = 'Name'
        # when
        # then
        with self.assertRaises(ValueError):
            dataset.add_column(column_name, None)

    def test_should_drop_column(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        column_name = "Name"

        # when
        dataset.drop_column(column_name)

        # then
        self.assertFalse(dataset.is_column_in_data(column_name))

    def test_not_allow_to_drop_non_existing_column(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        column_name = 'Not Existing Column'
        # when
        # then
        with self.assertRaises(ValueError):
            dataset.drop_column(column_name)

    def test_should_set_target_columns(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        target_columns = ['Name', 'City']

        # when
        dataset.set_target_columns(target_columns)

        # then
        self.assertEqual(len(dataset.get_target_columns()), 2)

    def test_not_allow_to_set_non_existing_column_as_target(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        target_columns = ['Name', 'Not Existing Column']

        # when
        # then
        with self.assertRaises(ValueError):
            dataset.set_target_columns(target_columns)

    def test_should_set_data_columns(self):
        # given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        data_columns = ['Name', 'City']

        # when
        dataset.set_data_columns(data_columns)

        # then
        self.assertEqual(len(dataset.get_data_columns()), 2)

    def test_not_allow_to_set_data_columns_which_are_target_columns(self):
        #given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        data_columns = ['Name', 'City']
        target_columns = ['Age', 'City']

        #when
        dataset.set_target_columns(target_columns)

        #then
        with self.assertRaises(ValueError):
            dataset.set_data_columns(data_columns)

    def test_should_get_columns(self):
        #given
        dataset = copy.deepcopy(DatasetTests.students_dataset)
        selected_columns = ['Name', 'City']

        #when
        data_columns = dataset.get_columns(selected_columns)
        print(data_columns.head())

        #then
        self.assertEqual(len(data_columns.columns),2)