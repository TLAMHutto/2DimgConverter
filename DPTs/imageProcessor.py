from transformers import AutoImageProcessor, DPTForDepthEstimation
import torch
import numpy as np
from PIL import Image


# Define the URL to fetch the image from the COCO dataset
file_path = '../img/original_image.jpg'  # Ensure 'your_image.jpg' is replaced with the actual image file name

# Open and save the image using PIL
image = Image.open(file_path)
image.save('./photos/imageProcessor/original_image.jpg', "JPEG")

# Load the pre-trained AutoImageProcessor and DPTForDepthEstimation models
image_processor = AutoImageProcessor.from_pretrained("Intel/dpt-large")
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

# Prepare the image for the model by encoding it with the image processor
inputs = image_processor(images=image, return_tensors="pt")

# Perform depth estimation on the image using the DPTForDepthEstimation model
with torch.no_grad():
    outputs = model(**inputs)
    predicted_depth = outputs.predicted_depth

# Interpolate the predicted depth to the original image size
prediction = torch.nn.functional.interpolate(
    predicted_depth.unsqueeze(1),
    size=image.size[::-1],  # Resizing to the original size of the image
    mode="bicubic",
    align_corners=False,
)

# Visualize the prediction
output = prediction.squeeze().cpu().numpy()
formatted = (output * 255 / np.max(output)).astype("uint8")
depth = Image.fromarray(formatted)
depth.save('./photos/imageProcessor/processed_depth.jpg', "JPEG")