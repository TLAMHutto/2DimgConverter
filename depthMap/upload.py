# from ipywidgets import GridspecLayout
# import ipywidgets as widgets

# grid_options = GridspecLayout(5, 4)

# file_name = {}
# file_name['name'] = ''
# file_name['depth'] = ''
# file_name['stl'] = ''
# def import_clicked(change):

#     if change.name == 'value':
#         # print('import')

#         file_name['name'] = list(change.new.keys())[0]
#         # print(file_name)

#     if file_name['name'] != '':
#           # with open("./userimg", "wb") as fp:
#           with open("/content/userimg", "wb") as fp:
#               fp.write(import_button.value[file_name['name']]['content'])

#           print('Uploaded')

#           grid_options[1, 2] = widgets.Label(str(file_name['name']) + ' uploaded')
#           grid_options[2, 2] = widgets.Label('')
#           grid_options[3, 2] = widgets.Label('')

#           file_name['depth'] = "".join(str(file_name['name']).split('.')[:-1]) + '_depth.png'
#           file_name['stl'] = "".join(str(file_name['name']).split('.')[:-1]) + '.stl'

# import_button = widgets.FileUpload(
#     # accept='.jpeg', '.jpg', .
#     multiple=False,
# )

# import_button.style.button_color = '#ededed'
# import_button.description = 'Upload Image'
# import_button.observe(import_clicked)

import os
import ipywidgets as widgets
from IPython.display import display
import torch
# import ZoeDepth as zoe
from PIL import Image
import matplotlib.pyplot as plt

# Define the directory where images are located
image_dir = '../img'


file_name = {}
file_name['name'] = ''
file_name['depth'] = ''
file_name['stl'] = ''

# List all files in the directory
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Rename the first image file to 'original_image.jpg'
if image_files:
    # Assume you want to rename the first file
    first_image_path = os.path.join(image_dir, image_files[0])
    
    # New name with path
    new_image_path = os.path.join(image_dir, 'original_image.jpg')
    
    # Open the image to ensure it's valid and save it under the new name
    image = Image.open(first_image_path)
    image.save(new_image_path, 'JPEG')

    # If you want to replace the old file, remove it after saving the new one
    if first_image_path != new_image_path:
        os.remove(first_image_path)

    print(f"Renamed '{image_files[0]}' to 'original_image.jpg'")
else:
    print("No image files found in the directory.")

# Create a dropdown to select an image file
dropdown = widgets.Dropdown(
    options=image_files,
    description='Select Image:',
    disabled=False,
)

# Display the dropdown
display(dropdown)

# Define what happens when an image is selected
def on_image_select(change):
    if change['type'] == 'change' and change['name'] == 'value':
        file_path = os.path.join(image_dir, change['new'])
        with open(file_path, 'rb') as file:
            image_content = file.read()
        # print(f'{change["new"]} selected and read from {image_dir}')

# Observe changes in the dropdown selection
dropdown.observe(on_image_select)

# If you need a grid layout, you can add other widgets or information in positions
grid_options = widgets.GridspecLayout(5, 4)
grid_options[0, 0] = dropdown
grid_options[1, 0] = widgets.Label('Image will be shown upon selection')

# zoe = torch.hub.load(".", "ZoeD_N", source="local", pretrained=True)
# dependencies = {}
#     # zoe = zoe.to('cuda')
# dependencies['zoe'] = zoe.to('cuda')

print('Successfully upload to project structure...')