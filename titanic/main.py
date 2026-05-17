import pandas as pd


def create_submission_csv(pred, index):
    submission = pd.DataFrame()
    submission['PassengerId'] = index
    submission['Survived'] = pred
    submission.to_csv('submission.csv', index=False)




