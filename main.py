from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb

# def test_exception():
#     try:
#         logging.info("This is a info message")
#         a = 1 / 0
#     except Exception as e:
#         raise SensorException(e, sys)

if __name__ == "__main__":

    file_path = r"C:\ML Projects\Sensor-Fault-Detection-\APS Dataset.csv"
    database_name = "Sensor_data"
    collection_name = "sensor"

    dump_csv_file_to_mongodb(file_path, database_name, collection_name)







    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
        
