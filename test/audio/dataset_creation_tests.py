from unittest import TestCase

from src.gender_recognition.audio.audio_dataset_creation import AudioDatasetCreator


class DatasetCreationTests(TestCase):
    def test_generate_dataset(self):
        #given
        dataset_creator = AudioDatasetCreator('dummy_root')

        #when
        dataset = dataset_creator.generate_dataset()

        #then
        self.assertNotEqual(dataset, None)
        dataset.save('dataset.csv')