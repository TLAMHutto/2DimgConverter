import os
import tkinter as tk
from tkinter import filedialog, messagebox, Toplevel
from PIL import Image, ImageTk
import subprocess
from functools import partial
from processing import process_AIP, process_DFE, process_PCD

# Define the directory where images are located
image_dir = '../img'
os.makedirs(image_dir, exist_ok=True)  # Ensure the directory exists

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Preview and Script Execution")
        
        self.image_dir = '../img'
        os.makedirs(self.image_dir, exist_ok=True)
        
        self.full_img = None  # Store full resolution image for preview
        self.photo_label = None
        self.resolution_label = None
        
        # Button to upload and preview an image
        self.upload_button = tk.Button(root, text="Upload and Preview", command=self.upload_and_preview)
        self.upload_button.pack(pady=10)
        
        # Dropdown menu to select and delete images
        self.dropdown = tk.StringVar(root)
        self.dropdown_menu = tk.OptionMenu(root, self.dropdown, "No files available")
        self.dropdown_menu.pack()

        # Button to delete selected images
        self.delete_button = tk.Button(root, text="Delete Selected Image", command=self.delete_selected_image)
        self.delete_button.pack(pady=10)

        # Buttons for DPT processes
        self.button_aip = tk.Button(root, text="Run AIP", command=process_AIP)
        self.button_aip.pack(pady=10)

        self.button_dfe = tk.Button(root, text="Run DFE", command=process_DFE)
        self.button_dfe.pack(pady=10)

        self.button_pcd = tk.Button(root, text="Run PCD", command=process_PCD)
        self.button_pcd.pack(pady=10)

        # Initialize the image list
        self.update_image_list()

    def upload_and_preview(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")])
        if file_path:
            self.full_img = Image.open(file_path)
            img = self.full_img.copy()
            img.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(img)
            
            if not self.photo_label:
                self.photo_label = tk.Label(self.root, image=photo)
                self.photo_label.pack(pady=20)
                self.photo_label.bind("<Button-1>", self.open_full_image)
            else:
                self.photo_label.config(image=photo)
            self.photo_label.image = photo
            
            resolution_text = f"Resolution: {self.full_img.size[0]}x{self.full_img.size[1]}"
            if not self.resolution_label:
                self.resolution_label = tk.Label(self.root, text=resolution_text)
                self.resolution_label.pack()
            else:
                self.resolution_label.config(text=resolution_text)
            
            self.save_image(self.full_img, file_path)
            self.update_image_list()

    def open_full_image(self, event):
        if self.full_img:
            top = Toplevel(self.root)
            top.title("Full Resolution Image")
            img = ImageTk.PhotoImage(self.full_img)
            lbl = tk.Label(top, image=img)
            lbl.image = img
            lbl.pack()

    def save_image(self, image, original_path):
    # Use a fixed file name instead of the original file name
        fixed_file_name = "original_image.jpg"
        save_path = os.path.join(self.image_dir, fixed_file_name)
        
        # Check if an image with the same name already exists and remove it
        if os.path.exists(save_path):
            os.remove(save_path)
        
        # Save the new image
        image.save(save_path)
        print(f"Image saved to {save_path}")

    def delete_selected_image(self):
        selected_file = self.dropdown.get()
        if selected_file and selected_file != "No files available":
            file_path = os.path.join(self.image_dir, selected_file)
            try:
                os.remove(file_path)
                messagebox.showinfo("Delete", f"Deleted {selected_file}")
                self.update_image_list()
            except OSError as e:
                messagebox.showerror("Error", f"Could not delete file: {e}")
        else:
            messagebox.showwarning("Delete", "No file selected or no files available to delete")

    def update_image_list(self):
        files = os.listdir(self.image_dir)
        self.dropdown_menu['menu'].delete(0, 'end')
        if files:
            for file in files:
                self.dropdown_menu['menu'].add_command(label=file, command=partial(self.dropdown.set, file))
            self.dropdown.set(files[0])
        else:
            self.dropdown.set("No files available")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()