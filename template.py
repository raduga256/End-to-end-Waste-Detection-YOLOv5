
import os
from pathlib import Path
import logging

# we shall usually use one logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "wasteDetection"    # root folder for my project

list_of_files = [                           #define files and folders that we need for the project
    f".github/workflows/.gitkeep",           # user inputs will be saved here for CI/CD deployment
    f"data/.gitkeep"
    f"{project_name}/__init__.py",          # constructor file
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/constant/config_entity.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    f"templates/index.html",
    f"research/trials.ipynb",
    f"app.py",
    f"Doickerfile",
    f"requirements.txt",
    f"setup.py"  
]

###
for filepath in list_of_files:
    filepath = Path(filepath)  # Path allows us to use forward slash(/) in path names

    filedir, filename = os.path.split(filepath)
    
    # Create file directory if it does not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file {filename}")
        
    # Create the files code
    if(not os.path.exists(filename)) or (os.path.getsize(filename)==0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filename}")
        
    else:
        logging.info(f"{filename} is already created/existing")
        