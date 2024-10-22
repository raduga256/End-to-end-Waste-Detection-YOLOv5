# Return types for config_entity  **Artifacts**

from dataclasses import dataclass


@dataclass
class DataIngestionArtifact:
    data_zip_file_path:str
    feature_store_path:str
    
# Define data validation artifacts class return type declared
@dataclass
class DataValidationArtifact:
    validation_status:bool
    

    