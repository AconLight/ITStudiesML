import os
import shlex
import subprocess
from src.serialization_flow.learnt_model_service import predict
import numpy as np

class AudioProcessor():

    def __init__(self, r_script_path) -> None:
        super().__init__()
        self.r_script_path = r_script_path


    def process_recorded_audio(self):
        data = subprocess.check_output(self.r_script_path)
        return self.edit_nan_and_inf_data(data)

    def process_audio_from_filepath(self, filepath):
        command = shlex.split(self.r_script_path + ' ' + os.path.join(os.getcwd(),filepath))
        data = subprocess.check_output(command)
        return self.edit_nan_and_inf_data(data)

    def edit_nan_and_inf_data(self, data):
        data = [float(i) for i in str(data).split("\"")[1].split(" ")]
        data = np.array(data)
        where_are_NaNs = np.isnan(data)
        data[where_are_NaNs] = 0
        data[data == -np.inf] = 0
        data[data == np.inf] = 0
        data = data.reshape(1, -1)
        return predict(data)[0]

    @staticmethod
    def create_audio_processor():
        return AudioProcessor('Rscript /home/hyphe/WFTIMS/MachineLearning/ITStudiesML/src/gender_recognition/audio/audio.R')
