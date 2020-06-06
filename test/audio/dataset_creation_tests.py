from unittest import TestCase

from src.gender_recognition.audio.audio_dataset_creation import AudioDatasetCreator, AudioDataset


class DatasetCreationTests(TestCase):
    def test_generate_dataset(self):
        #given
        dataset_creator = AudioDatasetCreator('dummy_root')

        #when
        dataset = dataset_creator.generate_dataset(save_path='dataset.csv')

        #then
        self.assertTrue(isinstance(dataset,AudioDataset))