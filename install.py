import os
import sys
import urllib.request
import subprocess

# === CONFIG ===
REPO_BASE_URL = "https://raw.githubusercontent.com/VexisTheFox/vexi-script/main/"
MAIN_SCRIPT = "main.py"
REQUIREMENTS = ["pygame", "requests"]

def download_script():
    url = REPO_BASE_URL + MAIN_SCRIPT
    print(f"Downloading {MAIN_SCRIPT}...")
    try:
        urllib.request.urlretrieve(url, MAIN_SCRIPT)
        print("Download complete.")
    except Exception as e:
        print(f"Download failed: {e}")
        sys.exit(1)

def install_requirements():
    print("Installing required packages...")
    for package in REQUIREMENTS:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def run_script():
    print(f"Running {MAIN_SCRIPT}...")
    subprocess.run([sys.executable, MAIN_SCRIPT])

def main():
    download_script()
    install_requirements()
    run_script()

if __name__ == "__main__":
    main()
