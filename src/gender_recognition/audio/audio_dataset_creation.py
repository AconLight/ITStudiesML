import os

import librosa

from src.gender_recognition.audio.audio import AudioProcessor
from src.gender_recognition.audio.audio_training_examples import AudioSampleGenerator
import pandas as pd

class DatasetClasses:
    SILENCE = 0
    MALE = 1
    FEMALE = 2

class AudioDataset():

    def __init__(self) -> None:
        super().__init__()
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def generate_dataset(self):
        return pd.DataFrame(data=self.rows)

    def save(self,path):
        self.generate_dataset().to_csv(path)

class AudioDatasetCreator:
    #
    #   root_directory - contains
    #
    #   Sample structure:
    #   root
    #   --> female
    #       - file1
    #   --> male
    #      ...
    #
    def __init__(self, root_directory) -> None:
        super().__init__()
        self.root_directory = root_directory
        self.audio_sample_generator = AudioSampleGenerator()
        self.audio_processor = AudioProcessor.create_audio_processor()


    def generate_dataset(self):
        dataset = AudioDataset()

        self.process_directory(dataset, "male")
        self.process_directory(dataset, "female")

        return dataset.generate_dataset()

    def process_directory(self, dataset, directory_name):
        dir_path = os.path.join(self.root_directory, directory_name)
        files = self.get_files_in_current_directory(dir_path)
        for filename in files:
            filepath = os.path.join(dir_path, filename)

            window_is_person_pairs, sampling_rate = self.audio_sample_generator.generate_audio_window_is_person_pairs_for_audio(filepath)

            for window_is_person_pair in window_is_person_pairs:
                audio, is_person = window_is_person_pair
                filename = self.save_temporary_audio(audio, sampling_rate)

                row = self.audio_processor.process_audio_from_filepath(filename)
                row = list(row)

                if is_person and directory_name == "male":
                    row.append(DatasetClasses.MALE)
                elif is_person and directory_name == "female":
                    row.append(DatasetClasses.FEMALE)
                else:
                    row.append(DatasetClasses.SILENCE)

                dataset.add_row(row)

    def get_files_in_current_directory(self, directory):
        return [f for f in os.listdir(directory)]

    def save_temporary_audio(self, audio_samples, sampling_rate):
        filename = 'tmp.wav'
        librosa.output.write_wav(filename, audio_samples, sampling_rate)
        return filename