

from src.gender_recognition.audio.audio_dataset_creation import AudioDatasetCreator, AudioDataset



#given
dataset_creator = AudioDatasetCreator('dummy_root')

#when
dataset = dataset_creator.generate_dataset(save_path='dataset.csv')
