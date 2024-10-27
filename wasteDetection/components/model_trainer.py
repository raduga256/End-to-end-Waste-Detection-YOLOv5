import os,sys
import yaml
from wasteDetection.utils.main_utils import read_yaml_file
from wasteDetection.logger import logging
from wasteDetection.exception import AppException
from wasteDetection.entity.config_entity import ModelTrainerConfig
from wasteDetection.entity.artifacts_entity import ModelTrainerArtifact


# Model Trainer components and functionality
class ModelTrainer:
    def __init__(self, 
                 model_trainer_config: ModelTrainerConfig):
        
        #Initalize the model trainer attributes
        self.model_trainer_config = model_trainer_config
        
    #  Iniate model trainer
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            
            logging.info("Unzipping data")
            
            # Running command line parsing. Just like in the Colab notebook
            os.system("unzip waste_data.zip")     # Unzip data zip file from src directory::: data folder should already exist
            os.system("rm waste_data.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            # Read waeights file and remove '.pt' extension
            ### You Must Have First downloaded the Yolov5 Model into the CWD
            # Run the following command in CMD/Terminal !git clone https://github.com/ultralytics/yolov5.git  # clone repo
                #1. delete .git file in the downloded model folder:: navigate there and delete to avoid having a double .git file in the project
                #2. copy the  requirements.txt from dowmloaded Yolov5 repo file to the project requirements file.
                #3. delete the artifacts folder b4 re-installation of pip install -r requirements.txt
                #4. install all the updated requirements using pip install -r requirements.txt
            
            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            # Update the yolov5 yaml file with the adjusted number of classes
            # If file does not exist, it will be created by -read_yaml_file **helper function
            config = read_yaml_file(f"yolov5/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            # Save the updated yaml file with a customized configuration name for new model
            with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            # constant for number of training epochs set to 30
            os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            
            # yolov5/runs folder should be created automatically on training the model
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            
            #Create mode trainer artifacts folder
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            
            logging.info("Start copy of created yolov5/runs folder")
            # This depends on cloning the yolov5 repo on every run--> python app.py because its always deleted
            # Run the following command in CMD/Terminal!git clone https://github.com/ultralytics/yolov5.git  # clone repo
            
            # delete.git file in the downloded model folder:: navigate there and delete to avoid having a double.git file in the project
            # copy the  requirements.txt from dowmloaded Yolov5 repo file to the project requirements file.
            # delete the artifacts folder b4 re-installation of pip install -r requirements.txt
            # install all the updated requirements using pip install -r requirements.txt
            os.system(f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
            logging.info("Deleting residue files -rf yolov5/runs train, valid, data.yaml")
            # delete all these files from the src root directory
            os.system("rm -rf yolov5/runs")
            os.system("rm -rf train")
            os.system("rm -rf valid")
            os.system("rm -rf data.yaml")

            # Initialize the model_trainer_artifact object with best weights
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov5/best.pt",)

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise AppException(e, sys)
        
        