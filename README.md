## Railway Station Ticket Barrier Classification Model

![Project Banner](https://github.com/GorPiliposyan/subway-ticket-barrier-state-detection/blob/main/banner_img.jpg)

### Task Description

The task aimed to create an open/closed classification model for ticket barriers ("gates") at railway stations. The provided images in a .zip file were used to build this model. The model's objective was to accurately determine whether a gate in an image is open or closed. It was crucial for the model to generalize well for unseen gate types, considering the provided data was only a subset of potential gate types.

### Approach Overview

- **Model Preparation Jupyter Notebook:** The process of creating the classification model was detailed in the `model_preparation.ipynb` notebook. This notebook includes comprehensive steps for data preparation, model training, and evaluation. Comments throughout the notebook elaborate on key decisions and metrics supporting the model's adequacy.

- **Model Deployment Preparation:**
  - Created a `Model()` class in `model.py`: This class wraps the trained model and includes a `predict()` method to run inference on a list of image tensors, providing "open" or "closed" labels for each image.
  - `model_run.py`: A Python script demonstrating the usage of the `Model()` class for inference on a set of images.

### Deliverables

Please find attached:
- `model_preparation.ipynb`: Detailed notebook showcasing the model creation process.
- `model.py` and `model_run.py`: Code files prepared for the engineering team, facilitating model usage.
- Model file: Necessary for running `model_run.py`.

The task was completed within the provided deadline and fulfills the requirements outlined in the task description.
