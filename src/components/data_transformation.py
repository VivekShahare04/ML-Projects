import sys
import os
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

from src.exception import customexception
from src.logger import Logger

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            numerical_columns = ['writing_score','reading_score']
            categorical_columns = ['gender','race/ethnicity','parental level of education','lunch','test preparation course']

            num_pipeline =Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )

            logging.info("Numerical columns are available")
            logging.info("Categorical columns are available")

            preprocessor = ColumnTransformer([
                ("num",num_pipeline,numerical_columns),
                ("cat",cat_pipeline,categorical_columns)
            ])

            return preprocessor

        except Exception as e:
            raise customexception(e,sys)