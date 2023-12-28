## Railway Station Ticket Barrier Classification Model


![Project Banner](https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/banner_img.gif)

### Task Description

The task aimed to create an open/closed classification model for ticket barriers ("gates") at railway stations. Some part of the images in the dataset used to build this model were provided privately, while the rest were acquired through web-scraping. The model's objective was to accurately determine whether a gate in an image is open or closed. It was crucial for the model to generalize well for unseen gate types, considering the provided data was only a subset of potential gate types.


#


### Tech Stack

- **Python**
- **PyTorch**
- **Ultralytics YOLOv8**
- **OpenCV**

<img align="left" alt="Java" width="30px" style="padding-right:10px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/Python-logo-notext.svg"/>
<img align="left" alt="Java" width="30px" style="padding-right:10px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/PyTorch_logo_icon.svg"/>
<img align="left" alt="Java" width="100px" style="padding-right:10px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/UltralyticsYOLO_full_blue.svg"/>
<img align="left" alt="Java" width="30px" style="padding-right:10px;" src="https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/Images/OpenCV_Logo.svg"/>
  

### 

#

### Approach Overview

- **Model Preparation Jupyter Notebook:** The process of creating the classification model was detailed in the `model_preparation.ipynb` notebook. This notebook includes comprehensive steps for data preparation, model training, and evaluation. Comments throughout the notebook elaborate on key decisions and metrics supporting the model's adequacy.

- **Model Deployment Preparation:**
  - Created a `Model()` class in `model.py`: This class wraps the trained model using a `load_model()` method for loading the model and includes a `predict()` method to run inference on a list of image tensors, the output of which is a list of "open" or "closed" labels in binary format (0/1).
  - `model_run.py`: A Python script demonstrating the usage of the `Model()` class for inference on a set of images.


#



### Deliverables

**Main files:**
- `model_preparation.ipynb`: Detailed Jupyter Notebook showcasing in detail the model creation process with relevant comments and a discussion section in the end.
- `model.py`: Python code file containing the `Model()` class, prepared for software engineering teams to facilitate model usage. Necessary for running `model_run.py`.
- `model_run.py`: For demonstration of the usage of the `Model()` class in `model.py` file.
- `yolov8x_cls_custom.pt`: Ultralytics YOLOv8 custom trained 'yolov8x-cls.pt' model weights file. Necessary to run `model_run.py` file.

**Extra files:**
- `utils`: Folder with some helper functions I have used for "model_preparation.ipynb"
- `data`: Folder with all the staged the dataset has been taken through
- `results.csv`: File with training related info per epoch. (*Used in `model_preparation.ipynb`*)
