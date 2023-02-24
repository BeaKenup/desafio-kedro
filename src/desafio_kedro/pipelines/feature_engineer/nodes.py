"""
This is a boilerplate pipeline 'feature_engineer'
generated using Kedro 0.18.5
"""
import pandas as pd

def feature_engineer_test(preprocess_titanic_test:pd.DataFrame):
    remove_columns = ['PassengerId', 'Name']
    preprocess_titanic_test.dropna()
    preprocess_titanic_test = preprocess_titanic_test.drop(remove_columns,axis=1)
    preprocess_titanic_test = preprocess_titanic_test.dropna()

    sc_test = StandardScaler()
    test_data= sc_test.fit_transform(preprocess_titanic_test)
    test_data= sc_test.transform(preprocess_titanic_test)
    test_data=pd.DataFrame(test_data)

    return preprocess_titanic_test

def feature_engineer_train(preprocess_titanic_train:pd.DataFrame):
    x = preprocess_titanic_train[['Age_Baby', 'Age_Kid', 'Age_Young', 'Age_Adult', 'Age_Old', 'Embarked_C', 'Embarked_Q', 'Embarked_S', 'Sex_female', 'Sex_male', 'SibSp', 'Parch', 'Pclass']]
    y = preprocess_titanic_train[['Survived']]

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1) # 70% training and 30% test
    clfSVM = SVC(gamma='auto',kernel='rbf', random_state=1)
    clfSVM = clfSVM.fit(X_train,y_train)
    y_pred = clfSVM.predict(X_test)

    y_pred_RF_clfSVM =clfSVM.predict(test_data)
    y_pred_RF_clfSVM

    return preprocess_titanic_train
    
def result_titanic(feature_engineer_test:pd.DataFrame):
    y_pred_RF_clfSVM=pd.DataFrame(y_pred_RF_clfSVM)
    feature_engineer_test['Survived']=y_pred_RF_clfSVM
    result = feature_engineer_test

    result.dropna()





