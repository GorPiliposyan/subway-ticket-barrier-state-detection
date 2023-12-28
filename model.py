from ultralytics import YOLO
import numpy as np
import torch
import torchvision
import torchvision.transforms as transforms

class Model():
    """
    This class receives a trained model and implements a predict() method for inferrence.

    """

    def __init__(self):


        self.img_size = 160
        self.mean = [0.4283, 0.4232, 0.4222] # Update values later!!!! MAKE SURE THESE ARE UP TO DATE.
        self.std  = [0.1982, 0.1997, 0.1998] # Update values later!!!! MAKE SURE THESE ARE UP TO DATE.

        self.model = None
        self.predictions = []
        self.class_names = None
        self.transform = None

    # MAYBE LATER ADD A to() FUNCTIONALITY TO SEND THE MODEL AND DATA TO A GPU DEVICE
    # self.device = 'cuda' if torch.cuda.is_available() else 'cpu'

    def predict(self, x):

        # Forget previous predictions
        self.predictions = []

        # Transform inputs
        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(size=(self.img_size, self.img_size)),
            transforms.ToTensor(),
            # transforms.Normalize(mean = self.mean, std = self.std)
        ])

        # Make predictions
        for image_tensor in x:
            transformed_image = self.transform(image_tensor)
            results  = self.model(transformed_image, verbose=False)
            self._organise_outputs(results)

        return self.predictions


    def load_model(self, model):
        """
        Load the model if the user has only provided the path to the .pt file.
        """
        self.model = model

        if isinstance(self.model, str):
            self.model = YOLO(self.model)
            print('Model successfully loaded.')



    def _organise_outputs(self, results):

        # Organise the output
        self.class_names = results[0].names
        for i in range(len(results)):
            cls_probs = results[i].probs.tolist()
            prediction = self.class_names[np.argmax(cls_probs)]
            self.predictions.append(prediction)


    def _update_params(img_size, mean, std):
        """
        In case of using a model which was optimised for image size other than (160x160)
        we need to update self.img_size, img_size.mean and img_size.std parameters.
        """
        self.img_size = img_size
        self.mean = mean
        self.std = std
