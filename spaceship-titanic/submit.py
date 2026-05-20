import pandas as pd


def submit(predictions, index):
    results = pd.DataFrame()
    results['PassengerId'] = index
    results['Transported'] = predictions
    results.to_csv('submission.csv', index=False)