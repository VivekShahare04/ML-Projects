import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split 
from dataclasses import dataclass
from src.exception import customexception
from src.logger import logging
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionconfig:
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')
    raw_data_path:str = os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Entering data ingestion configuration')
        try:
            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info('Saved the dataset as csv file & train test is initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=45)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Ingestion is Completed')
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise customexception(e,sys)
        

if __name__ == '__main__':
    obj = DataIngestion()
    train_data,train_test=obj.initiate_data_ingestion()

    obj2 = DataTransformation()
    obj2.initiate_datatransformation(train_data,train_test)