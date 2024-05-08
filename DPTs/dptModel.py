import numpy as np
from PIL import Image
import torch
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
# Create a DPT feature extractor
feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-large")

# Create a DPT depth estimation model
model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")

# Specify the URL of the image to download
print('test')

# Set the path to the image file
file_path = '../img/original_image.jpg'  # Ensure 'your_image.jpg' is replaced with the actual image file name

# Open and save the image using PIL
image = Image.open(file_path)
image.save('./photos/dptModelPi/original_image.jpg', "JPEG")


pixel_values = feature_extractor(image, return_tensors="pt").pixel_values


# Use torch.no_grad() to disable gradient computation
with torch.no_grad():
    # Pass the pixel values through the model
    outputs = model(pixel_values)
    # Access the predicted depth values from the outputs
    predicted_depth = outputs.predicted_depth



# Interpolate the predicted depth values to the original size
prediction = torch.nn.functional.interpolate(
    predicted_depth.unsqueeze(1),
    size=image.size[::-1],
    mode="bicubic",
    align_corners=False,
).squeeze()

# Convert the interpolated depth values to a numpy array
output = prediction.cpu().numpy()

# Scale and format the depth values for visualization
formatted = (output * 255 / np.max(output)).astype('uint8')

# Create an image from the formatted depth values
depth = Image.fromarray(formatted)
depth.save('./photos/dptModelPi/dpt_depth.jpg', "JPEG")
