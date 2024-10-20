# ultize the workflows chart

import os
from dataclasses import dataclass
from datetime import datetime
from wasteDetection.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    # Create *Artifacts* root directory
    artifacts_dir: str = ARTIFACTS_DIR   #being imported from constant folder file
    

# Create and intialize training pipeline object
training_pipeline_config: TrainingPipelineConfig = TrainingPipelineConfig()


# artifacts/data_ingestion *folder* creation
# dataclass constructor for data ingestion pipeline
# Used to access some variables in the constants file or config.yaml file
@dataclass
class DataIngestionConfig:
    # create path to data_ingestion root folder
    data_ingestion_dir : str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )
    
    # create path to data_ingestion/data directory to save downloads to
    feature_store_file_path : str = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_FEATURE_STORE_DIR)
    
    #gdrive file sharing url
    data_download_url: str = DATA_DOWNLOAD_URL
