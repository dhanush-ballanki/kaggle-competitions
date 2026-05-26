import pandas as pd
import os 

DATASETS_PATH = os.path.join('.', 'datasets')


def fetch_data(filename):
    filepath = os.path.join(DATASETS_PATH, filename)
    data = pd.read_csv(filepath)
    return data

def create_submission_csv(pred, index):
    submission = pd.DataFrame()
    submission['id'] = index
    submission['sales'] = pred
    submission.to_csv('submission.csv', index=False)