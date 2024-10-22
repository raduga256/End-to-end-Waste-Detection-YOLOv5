# All configurations should be imported before
import sys
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.components.data_ingestion import DataIngestion

from wasteDetection.entity.config_entity import (DataIngestionConfig)
from wasteDetection.entity.artifacts_entity import (DataIngestionArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        #self.data_validation_config = DataValidationConfig()
        #self.model_trainer_config = ModelTrainerConfig()
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            # Instantiate and intialize the DataIngestion component class
            data_ingestion = DataIngestion(
                data_ingestion_config =  self.data_ingestion_config
            )

            # Call the initiate_data_ingestion method to download and extract the data from the URL
            # data_ingestion component and it returns the artifact object
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the data from URL")
            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return data_ingestion_artifact

        except Exception as e:
            raise AppException(e, sys)
        


    # Run the data pipeline
    def run_pipeline(self) -> None:
        try:
            logging.info(
                "Entered the run_pipeline method of TrainPipeline class"
            )
            data_ingestion_artifact = self.start_data_ingestion()
            # data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
            # model_trainer_artifact = self.start_model_training(data_validation_artifact)
            logging.info(
                "Exited the run_pipeline method of TrainPipeline class"
            )
            
        except Exception as e:
            raise AppException(e, sys)