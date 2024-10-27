# End-to-end-Waste-Detection-YOLOv5

Welcome to my comprehensive guide on implementing an end-to-end Object Detection project using the powerful YOLOv5 model! 🚀

In this Project, I'll take you through every step of the process, from data preparation and model training to deployment, 
enabling you to detect objects in images and videos with remarkable accuracy and efficiency.

▬▬▬▬ Contents of this Project/  ▬▬▬▬▬
 - Introduction
 - Project Demo
 - Github Repository Setup
 - Project Template Creation
 - Requirements Installation & Project Setup
 - Data Annotation
 - Notebook Expriement
 - Logging, Exception & Utils Modules
 - Project Workflows
 - Data Ingestion Component
 - Data Validation Component
 - Model Trainer Component
 - Prediction Pipeline & User App
 - Dockerization & AWS CICD Deployment
 - Azure CICD Deployment

## Workflows
1. constants
2. entity
3. components
4. pipelines
5. app.py

## STEPS:
Clone the repository

### STEP 01- Create a conda environment after opening the repository

### STEP 02- install the requirements
pip install -r requirements.txt

# Train Custom YOLOv5 Detector

### Next, we'll fire off training!


Here, we are able to pass a number of arguments:
- **img:** define input image size
- **batch:** determine batch size
- **epochs:** define the number of training epochs. (Note: often, 3000+ are common here!)
- **data:** set the path to our yaml file
- **cfg:** specify our model configuration
- **weights:** specify a custom path to weights. (Note: you can download weights from the Ultralytics Google Drive [folder](https://drive.google.com/open?id=1Drs_Aiu7xx6S-ix95f9kNsA6ueKRpN2J))
- **name:** result names
- **nosave:** only save the final checkpoint
- **cache:** cache images for faster training

## Cloning Yolov5 repo into src directory
There after cloning the repository, we make adustments to the configuration files to fit our custom data set and number of classes, 

-read the yolov5.yaml file for the selected model and make a new copy of it.
- adjust the number of classes in the above configuration file while stating the number of epochs we want to run, path to the best model weights, etc

### STeps:
    os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
            
            #Create mode trainer artifacts folder
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            
            # This depends on cloning the yolov5 repo on every run--> python app.py
            # Run the following command in CMD/Terminal!git clone https://github.com/ultralytics/yolov5.git  # clone repo
            
            # delete.git file in the downloded model folder:: navigate there and delete to avoid having a double.git file in the project
            # copy the  requirements.txt from dowmloaded Yolov5 repo file to the project requirements file.
            # delete the artifacts folder b4 re-installation of pip install -r requirements.txt
            # install all the updated requirements using pip install -r requirements.txt