# All configurations should be imported before
import sys
from wasteDetection.logger import logging
from wasteDetection.exception import AppException

from wasteDetection.components.data_ingestion import DataIngestion
from wasteDetection.components.data_validation import DataValidation
from wasteDetection.components.model_trainer import ModelTrainer


from wasteDetection.entity.config_entity import (DataIngestionConfig, DataValidationConfig, ModelTrainerConfig)
from wasteDetection.entity.artifacts_entity import (DataIngestionArtifact, 
                                                    DataValidationArtifact, 
                                                    ModelTrainerArtifact)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
    
    # process the data ingestion configuration pipeline
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try: 
            logging.info(
                "Entered the start_data_ingestion method of TrainPipeline class"
            )
            logging.info("Getting the data from URL")

            # Intialize the Artifact object for data Ingestion
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
        

    # Initiate data validation configuration pipeline
    def start_data_validation(
        self, data_ingestion_artifact: DataIngestionArtifact
    ) -> DataValidationArtifact:
        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            # Iniate the data validation component
            data_validation = DataValidation(
                data_ingestion_artifact=data_ingestion_artifact,
                data_validation_config=self.data_validation_config,
            )

            # Initialize artifact from this step
            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Performed the data validation operation")

            logging.info(
                "Exited the start_data_validation method of TrainPipeline class"
            )

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys) from e
    

    ####           MODER TRAINER #####
    def start_model_trainer(self
    ) -> ModelTrainerArtifact:
        
        try:
            model_trainer = ModelTrainer(
                model_trainer_config=self.model_trainer_config,
            )
            
            logging.info("Entered the initiate_model_trainer method of TrainPipeline class")
            #Initialize Model Trainer Artifact
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact

        except Exception as e:
            raise AppException(e, sys)
    
    
    # Run the data pipeline
    def run_pipeline(self) -> None:
        try:
            logging.info(
                "Entered the run_pipeline method of TrainPipeline class"
            )
            data_ingestion_artifact = self.start_data_ingestion()
           
            data_validation_artifact = self.start_data_validation(
               data_ingestion_artifact=data_ingestion_artifact
            )
            
            # Model Trainer is dependent on data validation status == True. Check this condition
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            
            else:
                raise Exception("Your data is not in correct format")
           
            logging.info(
                "Exited the run_pipeline method of TrainPipeline class"
            )
            
        except Exception as e:
            raise AppException(e, sys)