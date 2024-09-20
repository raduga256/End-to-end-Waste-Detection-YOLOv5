# Local packages installation file

from setuptools import find_packages, setup

setup(
    name= "wasteDetection",
    version="0.0.0",
    author="Paul N",
    author_email="ntalops@yahoo.com",
    packages=find_packages(),
    install_requires = []
)

# Create conda environment
    # conda create -n waste-dectection python=3.8
    # actiave the env
    
    # Go to setting --> select the correct python version b4 installing requirements.txt
    # install requirements.txt file into the virtual env
    # then run setup.py
    
