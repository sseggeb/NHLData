import kaggle
import os

kaggle.api.authenticate()

dataset_identifier = "mexwell/nhl-database"

download_path = "kaggledownload/"

os.makedirs(download_path, exist_ok=True)

print(f"Downloading {dataset_identifier} to {download_path}...")

try:
    kaggle.api.dataset_download_files(dataset_identifier, path=download_path, unzip=True)
    print(f"Downloaded {dataset_identifier} to {download_path} and unzipped successfully.")

except Exception as e:
    print(f"an error occurred: {e}")

    print(f"files in {download_path}: {os.listdir(download_path)}")