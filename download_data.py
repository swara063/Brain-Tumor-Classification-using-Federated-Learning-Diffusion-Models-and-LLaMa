import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset():
    """
    Download dataset from Kaggle and unzip it into the data directory.
    """
    # Initialize Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Define the Kaggle dataset path and destination file
    dataset_path = 'your-kaggle-username/dataset-name'  # Replace with actual "username/dataset-name"
    download_path = 'data/original_dataset.zip'

    # Create a 'data' directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # Download the dataset
    print("Downloading dataset...")
    api.dataset_download_files(dataset_path, path='data', unzip=False)

    # Unzip the dataset
    print("Extracting dataset...")
    with zipfile.ZipFile(download_path, 'r') as zip_ref:
        zip_ref.extractall('data/original_dataset')
    print("Download and extraction complete.")

    # Clean up the downloaded zip file
    os.remove(download_path)

if __name__ == "__main__":
    download_dataset()
