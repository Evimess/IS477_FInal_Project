import os
import zipfile
import hashlib
import glob
import shutil

# Configuration: Map dataset slug to (Expected CSV Name, Unique Zip Name)
DATASETS = {
    "ulrikthygepedersen/fastfood-nutrition": ("fastfood.csv", "fastfood.zip"),
    "shrutisaxena/food-nutrition-dataset": ("food.csv", "usda_food.zip"),
    "utsavdey1410/food-nutrition-dataset": ("FOOD-DATA-GROUP1.csv", "yazio_food.zip")
}

def calculate_hash(file_path):
    """Calculates SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def find_and_move_file(target_filename):
    """
    Searches for a file recursively in the current directory.
    If found in a subfolder, moves it to the root.
    """
    if os.path.exists(target_filename):
        return True
    
    # Search in subdirectories
    for root, dirs, files in os.walk("."):
        if target_filename in files:
            source_path = os.path.join(root, target_filename)
            print(f"Found {target_filename} in {root}, moving to root...")
            shutil.move(source_path, target_filename)
            return True
    return False

def download_and_extract():
    print("Starting Data Acquisition...")
    
    # 1. Download and Extract
    for slug, (target_csv, zip_name) in DATASETS.items():
        if os.path.exists(target_csv):
            print(f"[{target_csv}] already exists. Skipping download.")
            continue

        print(f"\nAcquiring {slug}...")
        
        # Download with specific filename to avoid collisions
        # We assume the user has kaggle installed. 
        # Since the API doesn't let us name the zip easily via CLI args in all versions, 
        # we will download it, then identify the downloaded zip file.
        
        # Clean up any existing zips to avoid confusion
        os.system("rm -f *.zip") 
        
        exit_code = os.system(f"kaggle datasets download -d {slug}")
        if exit_code != 0:
            print(f"Error downloading {slug}. Check your Kaggle API key.")
            continue
            
        # Find the downloaded zip (it will be the only one, or named after the slug)
        # Usually slug 'user/dataset' becomes 'dataset.zip'
        default_zip = slug.split('/')[-1] + ".zip"
        
        if os.path.exists(default_zip):
            print(f"Extracting {default_zip}...")
            with zipfile.ZipFile(default_zip, 'r') as zip_ref:
                zip_ref.extractall(".")
            os.remove(default_zip)
        else:
            print(f"Could not find zip file for {slug}")

        # Ensure the file is in the root directory
        if not find_and_move_file(target_csv):
            print(f"WARNING: Could not find {target_csv} after extraction!")

    # 2. Final Integrity Check
    print("\n--- Integrity Report (SHA-256) ---")
    missing_files = []
    for slug, (target_csv, _) in DATASETS.items():
        if os.path.exists(target_csv):
            print(f"✅ {target_csv}: {calculate_hash(target_csv)[:16]}...")
        else:
            print(f"❌ {target_csv} is MISSING.")
            missing_files.append(target_csv)
    
    if missing_files:
        print(f"\nCurrent Directory Contents: {os.listdir('.')}")
        raise FileNotFoundError(f"Missing required files: {missing_files}")

if __name__ == "__main__":
    download_and_extract()