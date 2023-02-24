"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from desafio_kedro.pipelines import pre_processing as pp
from desafio_kedro.pipelines import feature_engineer as fe

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    pre_processing_pipeline = pp.create_pipeline()
    feature_engineer_pipeline = fe.create_pipeline()
    
    return {
        "pp": pre_processing_pipeline,
        "fe": feature_engineer_pipeline,
        "__default__": pre_processing_pipeline + feature_engineer_pipeline    }
