import os
import sys
import shutil
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import DataValidationConfig
from wasteDetection.entity.artifacts_entity import (DataValidationArtifact,
                                                    DataIngestionArtifact)


#Initialization of data validation class
class DataValidation:
    def __init__(self,
                 data_validation_config: DataValidationConfig,
                 data_ingestion_artifact: DataIngestionArtifact
                 ):
    
        try: 
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact= data_ingestion_artifact
                    
        except Exception as e:
            raise AppException(e, sys)
        
    # Check if the artifacts from the faeture store are present
    def validate_all_files_exist(self)-> bool:
            try:
                validation_status = None

                # get list of flies in feature_store dir
                all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
                
                # check for train, valid, data.yaml files and update validation status.txt 
                logging.info("Checking for data ingestion artifacts outputs")
                for file in all_files:
                    if file not in self.data_validation_config.required_file_list:
                        
                        #set validation status to false if any of teh 3 files required by yolov5 are missing
                        validation_status = False
                        os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                        
                        #open the file status.txt and update validation status
                        with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    else:
                        validation_status = True
                        os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                        
                        #open the file status.txt and update validation status
                        with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                            f.write(f"Validation status: {validation_status}")

                return validation_status


            except Exception as e:
                raise AppException(e, sys)
            
    # Create the main method to intiate the entire validation process
    def initiate_data_validation(self) -> DataValidationArtifact: 
        logging.info("Entered initiate_data_validation method of DataValidation class")
        
        try:
            # get the validation status from status.txt readings
            status = self.validate_all_files_exist()
            
            # parse the status to the DATA VALIDATION @dataclass status attribute
            data_validation_artifact = DataValidationArtifact(
                validation_status=status)

            logging.info("Exited initiate_data_validation method of DataValidation class")
            logging.info(f"Data validation artifact: {data_validation_artifact}")

            # if validation is successful, copy the data zip file to the current directory i.e src root directory for easy path manipulation
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact

        except Exception as e:
            raise AppException(e, sys)