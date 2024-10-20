#
import os
import sys
import zipfile
import gdown

from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import DataIngestionConfig
from wasteDetection.entity.artifacts_entity import DataIngestionArtifact

#
class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise AppException(e, sys)
   
        # download data from source
    def download_file(self)-> str:
        '''
        Fetch data from source/url
        '''
    
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir  # change this to local 
            #create directory if it doesn't exist for artifacts/dataingestion
            os.makedirs(zip_download_dir, exist_ok=True)
            
            # provide new name for the download file
            data_file_name = "waste-data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            
            
            logging.info(f"Downloading data from {dataset_url} into {zip_download_dir}")        
            
            # Download from gdrive storage
            file_id = dataset_url.split("/")[-2]
            # Construct the download URL
            prefix_download_url = f"https://drive.google.com/uc?id={file_id}&export=download"

            # Download the file into a local dir  # Change this to your desired file name and extension
            gdown.download(prefix_download_url, zip_download_dir)
            
            return zip_file_path
            
        except Exception as e:
            raise e

    # Extract the the downloaded zip file INTO **feature_store** folder
    def extract_zip(self, zip_file_path:str) -> str:
        '''
        zip_file_path: str
        Extracts zip file to the directory specified in extract_dir directory
        Function returns None
        '''
        
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            # create extract directory incase it doesn't exist
            os.makedirs(feature_store_path, exist_ok=True)
            # read zip file and extract it
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(feature_store_path)
            logging.info(f"Extracting zip file : {zip_file_path} into {feature_store_path}")
            
            #return feature_store_path
            
        except Exception as e:
            raise AppException(e, sys)
        
    # Load the data from **feature_store** into the data lake
    def initiate_data_feature_store(self) -> DataIngestionArtifact:
        
        logging.info(f"Entered intiate_data_ingestion method of DataIngestion class")
        
        try:
            # Call the function to download the zip file
            zip_file_path = self.download_file()
            
            
            # Call the function to extract the zip file
            faeture_store_path = self.extract_zip(zip_file_path)
            
            # Create and return an object of DataIngestionArtifact
            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path=zip_file_path, 
                feature_store_path=faeture_store_path
            )
            
            return data_ingestion_artifact
        
        except Exception as e:
            raise AppException(e, sys)
    