"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_titanic_train, preprocess_titanic_test

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = preprocess_titanic_train,
            inputs = 'train',
            outputs = 'pp_titanic_train',
            name = 'preprocess_titanic_train'
        )
    ])
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = preprocess_titanic_test,
            inputs = 'test',
            outputs = 'pp_titanic_test',
            name = 'preprocess_titanic_test'
        )
    ])