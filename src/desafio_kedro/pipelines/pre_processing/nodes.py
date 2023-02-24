"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.4
"""

import pandas as pd

def preprocess_titanic_train(train:pd.DataFrame):
    train = train.drop(columns=['Name', 'Fare','Ticket','Cabin'])
    train = train.dropna()

    bins = [0, 5, 17, 25, 50, 80] 
    labels = ['Baby', 'Kid', 'Young', 'Adult', 'Old']
    train['Age'] = pd.cut(train ['Age'], bins = bins, labels=labels)

    dummies = ['Age', 'Embarked', 'Sex']
    dummy_data = pd.get_dummies(train[dummies])

    train = pd.concat([train, dummy_data], axis = 1)
    train.drop(dummies, axis=1, inplace=True)
    
    return train

def preprocess_titanic_test(test:pd.DataFrame):
    test = test.drop(columns=['Fare','Ticket','Cabin'])
    test = test.dropna()

    bins = [0, 5, 17, 25, 50, 80] 
    labels = ['Baby', 'Kid', 'Young', 'Adult', 'Old']
    test['Age'] = pd.cut(test ['Age'], bins = bins, labels=labels)
    
    dummies = ['Age', 'Embarked', 'Sex']
    dummy_data = pd.get_dummies(test[dummies])

    test = pd.concat([test, dummy_data], axis = 1)
    test.drop(dummies, axis=1, inplace=True)

    return test

