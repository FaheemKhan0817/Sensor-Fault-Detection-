from sensor.configuration.mongodb_connection import MongoDBClient
from sensor.exception import SensorException
import os , sys
from sensor.logger import logging
#from  sensor.utils import dump_csv_file_to_mongodb_collecton
#from sensor.entity.config_entity  import TrainingPipelineConfig,DataIngestionConfig

from sensor.pipeline.training_pipeline import TrainPipeline

if __name__ == "__main__":



    training_pipeline = TrainPipeline()
    training_pipeline.run_pipeline()









  












    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)