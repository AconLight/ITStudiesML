from joblib import dump, load


def serialize_model(model, filename):
    dump(model, filename + '.joblib')


def deserialize_model(filename):
    return load(filename + '.joblib')
