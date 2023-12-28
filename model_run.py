from ultralytics import YOLO
import cv2
from model import Model
import torch
import torchvision
import torchvision.transforms as transforms

# Set a seed
torch.manual_seed(0)

# Get a custom model
yolov8x_cls_custom = YOLO('./yolov8x_cls_custom.pt')

# Instantiate a model object
my_model = Model()

# Load the model (Note: Can be either a preloaded model or directly the path to the source .pt file)
my_model.load_model(yolov8x_cls_custom)

# To run inference, provide path to a previously unseen sample data folder
sample_dataset_path = './data/sample_data' # './Your/Folder/Path/Here'

# Get the dataset as a torch.Tensor object
test_transforms = transforms.Compose([
    transforms.Resize(size=(160,160)),
    transforms.ToTensor(),
])

sample_dataset = torchvision.datasets.ImageFolder(root=sample_dataset_path, transform=test_transforms)
sample_loader  = torch.utils.data.DataLoader(dataset=sample_dataset, batch_size=8, shuffle=False)


# Make the inference in batches and print predictions as lists.
i = 0
for images_tensor, label in sample_loader:
    i += 1
    predictions = my_model.predict(images_tensor)
    print(f"\nBatch {i} - predictions:\n", predictions)