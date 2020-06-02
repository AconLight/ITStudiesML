import subprocess
from src.serialization_flow.learnt_model_service import predict
import numpy as np


def process_audio():
    data = subprocess.check_output(
        '"C:\\Program Files\\R\\R-4.0.0\\bin\\x64\\Rscript.exe" ..\\gender_recognition\\audio\\audio.R')
    data = [float(i) for i in str(data).split("\"")[1].split(" ")]

    # expected columns: ['meanfreq', 'sd', 'median', 'Q25', 'IQR', 'skew', 'kurt', 'sp.ent', 'sfm', 'mode', 'centroid', 'meanfun', 'minfun', 'maxfun', 'meandom', 'mindom', 'maxdom', 'dfrange', 'modindx']

    data = np.array(data)
    where_are_NaNs = np.isnan(data)
    data[where_are_NaNs] = 0
    data[data == -np.inf] = 0
    data[data == np.inf] = 0

    data = data.reshape(1, -1)

    return predict(data)[0]
