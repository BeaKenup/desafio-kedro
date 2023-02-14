"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import preprocess_titanic

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = preprocess_titanic,
            inputs = 'test',
            outputs = 'pp_titanic_dataset',
            name = 'preprocess_titanic'
        )
    ])
