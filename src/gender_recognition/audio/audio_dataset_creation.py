import os
import uuid

import librosa
import soundfile

from src.gender_recognition.audio.audio import AudioProcessor
from src.gender_recognition.audio.audio_training_examples import AudioSampleGenerator
import pandas as pd
import numpy as np


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
        return pd.DataFrame(data=np.concatenate(self.rows, axis=0))

    def save(self, path):
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
    def __init__(self, root_directory, audio_sample_generator=AudioSampleGenerator(sampling_rate=48000, window_size=12000), save_each_n_files = 5) -> None:
        super().__init__()
        self.root_directory = root_directory
        self.audio_sample_generator = audio_sample_generator
        self.audio_processor = AudioProcessor.create_audio_processor()
        self.counter = 0
        self.SAVE_EACH_N_FILES = save_each_n_files

    def generate_dataset(self, save_path=None):
        dataset = AudioDataset()

        self.process_directory(dataset, "male", save_path)
        self.process_directory(dataset, "female", save_path)

        return dataset

    def process_directory(self, dataset, directory_name, save_path):
        dir_path = os.path.join(self.root_directory, directory_name)
        files = self.get_files_in_current_directory(dir_path)
        for i,filename in enumerate(files):
            print("Processing directory " + directory_name + " file " + filename + "[" + str(i+1) + "/" + str(len(files))+ "]")
            filepath = os.path.join(dir_path, filename)

            window_is_person_pairs, sampling_rate = self.audio_sample_generator.generate_audio_window_is_person_pairs_for_audio(
                filepath)

            for window_is_person_pair in window_is_person_pairs:
                audio, is_person = window_is_person_pair

                filename = self.save_temporary_audio(audio, sampling_rate)
                row = self.audio_processor.process_audio_from_filepath(filename)
                os.remove(path=filename)

                if is_person and directory_name == "male":
                    row = np.append(row, [[DatasetClasses.MALE]], axis=1)
                elif is_person and directory_name == "female":
                    row = np.append(row, [[DatasetClasses.FEMALE]], axis=1)
                else:
                    row = np.append(row, [[DatasetClasses.SILENCE]], axis=1)

                dataset.add_row(row)

            self.counter += 1

            if save_path is not None and self.counter % self.SAVE_EACH_N_FILES == 0:
                print("Saving dataset after samples " + str(self.counter))
                dataset.save(save_path)

        if save_path is not None:
            print("Saving final dataset")
            dataset.save(save_path)

    def get_files_in_current_directory(self, directory):
        return [f for f in os.listdir(directory)]

    def save_temporary_audio(self, audio_samples, sampling_rate):
        filename = str(uuid.uuid4()) + 'tmp.wav'
        soundfile.write(filename, audio_samples, sampling_rate)
        return filename

