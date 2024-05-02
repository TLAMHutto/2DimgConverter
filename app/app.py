import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess

# Directory where images are saved
image_dir = '../img'
os.makedirs(image_dir, exist_ok=True)  # Ensure the directory exists

def upload_and_preview():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(img)
        
        global photo_label
        if 'photo_label' not in globals():
            photo_label = tk.Label(root, image=photo)
        else:
            photo_label.config(image=photo)
        
        photo_label.image = photo  # Keep a reference!
        photo_label.pack(pady=20)
        
        save_image(img, file_path)
        update_image_list()  # Update dropdown after uploading
        run_external_script()  # Run external script after upload
        process_button.pack(pady=10)

def save_image(image, original_path):
    file_name = os.path.basename(original_path)
    save_path = os.path.join(image_dir, file_name)
    image.save(save_path)
    print(f"Image saved to {save_path}")

def delete_selected_image():
    selected_file = dropdown.get()
    if selected_file and selected_file != "No files available":
        file_path = os.path.join(image_dir, selected_file)
        try:
            os.remove(file_path)
            messagebox.showinfo("Delete", f"Deleted {selected_file}")
            update_image_list()  # Update dropdown after deletion
            clear_image_preview()  # Clear the image preview
            run_external_script()  # Run external script after delete
        except OSError as e:
            messagebox.showerror("Error", f"Could not delete file: {e}")
    else:
        messagebox.showwarning("Delete", "No file selected or no files available to delete")

def update_image_list():
    files = os.listdir(image_dir)
    dropdown_menu['menu'].delete(0, 'end')
    if files:
        for file in files:
            dropdown_menu['menu'].add_command(label=file, command=lambda value=file: dropdown.set(value))
        dropdown.set(files[0])  # Set to first file in the list
    else:
        dropdown.set("No files available")  # Default message if no files

def clear_image_preview():
    global photo_label
    if 'photo_label' in globals():
        photo_label.config(image='')  # Clear the image display
        photo_label.pack_forget()  # Hide the label

def run_external_script():
    try:
        # Example: running a script located at ../depthMap/upload.py
        subprocess.run(['python', '../depthMap/upload.py'], check=True)
        print("Image ready to print depth map.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while uploadingt: {e}")

def processImg():
    global process_button
    process_button = tk.Button(root, text="Process Image", command=run_process_script)
    process_button.pack(pady=10)
    print("Process button created.")

def run_process_script():
    try:
        # Running the external script for processing the image
        subprocess.run(['python', '../depthMap/processImg.py'], check=True)
        print("Run process from app.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while processing image: {e}")

# Create the main window
root = tk.Tk()
root.title("Image Preview and Script Execution")

upload_button = tk.Button(root, text="Upload and Preview", command=upload_and_preview)
upload_button.pack(pady=10)

# Dropdown to select image for deletion
dropdown = tk.StringVar(root)
dropdown_menu = tk.OptionMenu(root, dropdown, "No files available")  # Default option
dropdown_menu.pack()

# Button to delete selected image
delete_button = tk.Button(root, text="Delete Selected Image", command=delete_selected_image)
delete_button.pack(pady=10)
processImg()

update_image_list()  # Initialize the dropdown list
  # Create a button for processing an image
# Start the GUI event loop
root.mainloop()
