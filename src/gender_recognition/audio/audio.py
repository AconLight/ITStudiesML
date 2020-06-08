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
        return predict(self.edit_nan_and_inf_data(data))[0]

    def process_audio_from_filepath(self, filepath):
        command = shlex.split(self.r_script_path + ' ' + '"{}\\{}"'.format(os.getcwd(),filepath))
        data = subprocess.check_output(command)
        return self.edit_nan_and_inf_data(data)

    def edit_nan_and_inf_data(self, data):
        data = [float(num) for num in str(data).split("\"")[-2].split()]
        data = np.array(data)
        where_are_NaNs = np.isnan(data)
        data[where_are_NaNs] = 0
        data[data == -np.inf] = 0
        data[data == np.inf] = 0
        data = data.reshape(1, -1)
        return data

    @staticmethod
    def create_audio_processor():
        return AudioProcessor('"C:\\Program Files\\R\\R-4.0.0\\bin\\x64\\Rscript.exe" "C:\\Users\\stz\\Documents\\GitHub\\ITStudiesML\\src\\gender_recognition\\audio\\audio.R"')
