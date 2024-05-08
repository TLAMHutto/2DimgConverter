import subprocess
import os

def process_AIP():
    try:
        # Define the path to the script
        script_path = '../DPTs/dptModel.py'
        # Change directory to the script's directory
        os.chdir(os.path.dirname(script_path))
        # Run the script
        subprocess.run(['python', os.path.basename(script_path)], check=True)
        print("dptModel.py executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing dptModel.py: {e}")
    finally:
        # Change back to the original directory
        os.chdir('../app')

def process_DFE():
    try:
        # Define the path to the script
        script_path = '../DPTs/imageProcessor.py'
        # Change directory to the script's directory
        os.chdir(os.path.dirname(script_path))
        # Run the script
        subprocess.run(['python', os.path.basename(script_path)], check=True)
        print("imageProcessor.py executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing imageProcessor.py: {e}")
    finally:
        # Change back to the original directory
        os.chdir('../app')

def process_PCD():
    try:
        # Define the path to the script
        script_path = '../converter/converter.py'
        # Change directory to the script's directory
        os.chdir(os.path.dirname(script_path))
        # Run the script
        subprocess.run(['python', os.path.basename(script_path)], check=True)
        print("converter.py executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing converter.py: {e}")
    finally:
        # Change back to the original directory
        os.chdir('../app')