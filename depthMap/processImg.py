import time
from PIL import Image
from matplotlib import widgets
import matplotlib.pyplot as plt
import numpy as np
import ipywidgets as widgets
import torch
import sys
sys.path.append('C:/Users/hutto/Desktop/Code/Python/dm-2-pcd/ZoeDepth')
sys.path.append('../app')
from upload import file_name, grid_options
import os
from PIL import Image

dependencies = {}
zoe = torch.hub.load(".", "ZoeD_N", source="local", pretrained=True)
dependencies['zoe'] = zoe.to('cuda')

def process_tile_size(img, tile_size, save_filter_images):
    print('processing tile size')
    num_x, num_y = tile_size
    M = img.height // num_x
    N = img.width // num_y

    filter_dict = {
        'right_filter': np.zeros((M, N)),
        'left_filter': np.zeros((M, N)),
        'top_filter': np.zeros((M, N)),
        'bottom_filter': np.zeros((M, N)),
        'top_right_filter': np.zeros((M, N)),
        'top_left_filter': np.zeros((M, N)),
        'bottom_right_filter': np.zeros((M, N)),
        'bottom_left_filter': np.zeros((M, N)),
        'filter': np.zeros((M, N))
    }

    # Dummy implementation of filter calculations
    # Populate filter_dict here with actual data processing
    for key in filter_dict:
        filter_dict[key] = np.random.rand(M, N)  # Random data for demonstration

    if save_filter_images:
        for key, filter_array in filter_dict.items():
            filter_image = Image.fromarray((filter_array * 255).astype("uint8"))
            filter_image.save(f'filter_{key}_{num_x}_{num_y}.png')
    
    return filter_dict

def combine_depth_maps(filters):
    print('combining depth maps')
    # Assuming filters is a list of dictionaries containing numpy arrays
    combined_depth = None
    for filter_dict in filters:
        for key, filter_array in filter_dict.items():
            if combined_depth is None:
                combined_depth = filter_array
            else:
                combined_depth += filter_array  # Combining logic can be adjusted

    # Normalize the result for demonstration purposes
    if combined_depth is not None:
        combined_depth = combined_depth / np.max(combined_depth) * 255
    
    return combined_depth.astype("uint8")


def process_clicked(change):
    total_steps = 10
    current_step = 1

    print(f'[{current_step}/{total_steps}] Process button was clicked..yay!')
    current_step += 1

    img = Image.open('../img/truck.jpeg')

    print(f'[{current_step}/{total_steps}] Image loaded successfully.')
    current_step += 1

    # Assuming ZoeD_N infer_pil method processes the image for depth estimation
    low_res_depth = dependencies['zoe'].infer_pil(img)
    print(f'[{current_step}/{total_steps}] Low resolution depth inferred.')
    current_step += 1

    low_res_scaled_depth = 2**16 - (low_res_depth - np.min(low_res_depth)) * 2**16 / (np.max(low_res_depth) - np.min(low_res_depth))
    low_res_depth_map_image = Image.fromarray((0.999 * low_res_scaled_depth).astype("uint16"))
    low_res_depth_map_image.save('zoe_depth_map_16bit_low.png')
    print(f'[{current_step}/{total_steps}] Low resolution depth map saved.')
    current_step += 1

    # Generate filters
    filters = []
    save_filter_images = True
    tile_sizes = [[4,4], [8,8]]

    for idx, tile_size in enumerate(tile_sizes):
        # Process each tile size
        filters.append(process_tile_size(img, tile_size, True))
        print(f'[{current_step}/{total_steps}] Processed tile size {tile_size}.')
        current_step += 1

    # Assuming the subsequent process here
    print(f'[{current_step}/{total_steps}] Starting combination of depth maps.')
    combined_result = combine_depth_maps(filters)
    print(f'[{current_step}/{total_steps}] Depth maps combined.')

    combined_image = Image.fromarray((2**16 * 0.999* combined_result / np.max(combined_result)).astype("uint16"))
    file_name = {
    'depth': 'output_image.png'  # Ensure this has a proper extension
}

    # Before saving, check if the 'depth' key exists and print the filename
    if 'depth' in file_name and isinstance(file_name['depth'], str):
        print("Saving to:", file_name['depth'])
        combined_image.save(file_name['depth'])
    else:
        print("Error: 'depth' key is missing or is not a string.")
    print(f'[{total_steps}/{total_steps}] Combined image saved and process completed.')

    # Display output images
    display_output_images(low_res_scaled_depth, combined_result)

def display_output_images(low_res_depth, high_res_depth):
    print('Displaying original low resolution result')
    plt.imshow(low_res_depth, cmap='magma')
    plt.axis("off")
    plt.show()

    print('\nDisplaying new high resolution result')
    plt.imshow(high_res_depth, cmap='magma')
    plt.axis("off")
    plt.show()

    print("Processing ended. Image processed.")

from IPython.display import display

def setup_process_button():
    process_button = widgets.Button(description="Process Image")
    process_button.on_click(process_clicked)
    display(process_button)

if __name__ == "__main__":
    setup_process_button()
