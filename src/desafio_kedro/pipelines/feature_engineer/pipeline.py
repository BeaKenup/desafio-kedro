"""
This is a boilerplate pipeline 'feature_engineer'
generated using Kedro 0.18.5
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import feature_engineer_test, feature_engineer_train, result_titanic

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = feature_engineer_train,
            inputs = 'preprocess_titanic_train',
            outputs = 'feature_engineer_train',
            name = 'feature_engineer_train'
        )
        , node(
            func = feature_engineer_test,
            inputs = 'preprocess_titanic_test',
            outputs = 'feature_engineer_test',
            name = 'feature_engineer_test'
        )
        , node(
            func = result_titanic,
            inputs = 'feature_engineer_test',
            outputs = 'result_titanic',
            name = 'result_titanic'
        )
    ])

