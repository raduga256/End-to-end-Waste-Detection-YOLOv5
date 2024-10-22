# Test logging
from wasteDetection.logger import logging

logging.info("Welcome to Paul's custom log")

# test command:: python app.py

from wasteDetection.pipeline.training_pipeline import TrainPipeline

# Create a new TrainingPipeline instance
obj = TrainPipeline()
obj.run_pipeline()