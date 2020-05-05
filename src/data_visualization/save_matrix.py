import pathlib
from os.path import sep

import numpy as np

path = str(pathlib.Path(__file__).parent.absolute().parent.parent) + sep + 'generated_graphs' + sep

def save_matrix(matrix, algorithm, db):
    np.savetxt(path + "confusion_matrix_" + db.split("/")[1] + "_" + algorithm, np.array(matrix), fmt='%1.3f')