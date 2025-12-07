import os
import zipfile
import hashlib

# Configuration
DATASETS = {
    "fastfood-nutrition": "ulrikthygepedersen/fastfood-nutrition",
    "food-nutrition-dataset": "shrutisaxena/food-nutrition-dataset", 
    "food-data-group1": "utsavdey1410/food-nutrition-dataset"
}

OUTPUT_FILES = [
    "fastfood.csv",
    "food.csv",
    "FOOD-DATA-GROUP1.csv"
]

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def download_and_extract():
    # 1. Download via Kaggle API
    for name, slug in DATASETS.items():
        print(f"Downloading {slug}...")
        exit_code = os.system(f"kaggle datasets download -d {slug}")
        if exit_code != 0:
            raise Exception(f"Failed to download {slug}. Ensure ~/.kaggle/kaggle.json exists.")
        
        # 2. Extract
        zip_name = slug.split('/')[-1] + ".zip"
        if os.path.exists(zip_name):
            with zipfile.ZipFile(zip_name, 'r') as zip_ref:
                zip_ref.extractall(".")
            # Clean up zip
            os.remove(zip_name)
    
    # 3. Rename specific files if necessary (The Kaggle downloads might have specific names)
    # Note: Based on your previous context, the files usually extract with their standard names.
    # If file names differ, add os.rename() logic here.

    # 4. Integrity Check
    print("\n--- Integrity Report (SHA-256) ---")
    for file in OUTPUT_FILES:
        if os.path.exists(file):
            print(f"{file}: {calculate_hash(file)}")
        else:
            print(f"WARNING: {file} is missing!")

if __name__ == "__main__":
    download_and_extract()