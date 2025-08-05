import os
import platform
import webbrowser
import requests
import pygame
from io import BytesIO
import urllib.request
import subprocess
import json
import sys
from datetime import datetime

# === CONFIG ===
GUNS_USERNAME = "vexi.tech"
TIKTOK_USERNAME = "@v3x1.tech"
SOUND_URL = "https://raw.githubusercontent.com/VexisTheFox/vexi-script/main/rawr.mp3"  # update this
VERSION_FILE = "vs_info.json"  # File to store version info remotely
SCRIPT_URL = "https://raw.githubusercontent.com/VexisTheFox/vexi-script/main/main.py"  # URL to the latest script (main.py)
GITHUB_BUILD_INFO_URL = "https://raw.githubusercontent.com/VexisTheFox/vexi-script/main/vs_info.json"  # URL for build info (vs_info.json)

# === Store version in the script ===
__version__ = "1.1"  # Version of the current script

# Function to check if the script is up to date by comparing it with the GitHub version info
def check_for_update():
    print("🔍 Checking for updates...")
    try:
        # Get the build info from the GitHub repository (latest version)
        latest_build_info = requests.get(GITHUB_BUILD_INFO_URL).json()
        latest_version = latest_build_info.get("version", "0.0")
        current_version = __version__  # Fetching the version from the script itself

        print(f"Current version: {current_version}")
        print(f"Latest version: {latest_version}")

        if latest_version != current_version:
            print("🆕 A new version is available!")
            return True, latest_version, latest_build_info
        else:
            print("✅ You have the latest version.")
            return False, current_version, latest_build_info
    except Exception as e:
        print(f"Error checking for updates: {e}")
        return False, __version__, {}

# Function to update the script by downloading the latest `main.py`
def update_script():
    print("🔄 Updating the script...")
    try:
        urllib.request.urlretrieve(SCRIPT_URL, "main.py")
        print("✅ Script updated successfully!")
    except Exception as e:
        print(f"Error updating the script: {e}")

# Function to restart the script after update
def restart_script():
    print("🔄 Restarting the script...")
    subprocess.run([sys.executable, "main.py"])

# === Existing Functions ===

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def show_menu():
    print("=== Terminal Tool ===")
    print("1. Show my guns.lol")
    print("2. Show my TikTok")
    print("3. Play Rawr")
    print("4. Check for Updates")
    print("5. Exit")

def show_guns():
    url = f"https://guns.lol/{GUNS_USERNAME}"
    print(f"Opening: {url}")
    webbrowser.open(url)

def show_tiktok():
    print(f"My TikTok is: {TIKTOK_USERNAME}")

def play_sound_from_url(url):
    try:
        print("Loading sound...")
        response = requests.get(url)
        response.raise_for_status()
        sound_data = BytesIO(response.content)

        pygame.mixer.init()
        pygame.mixer.music.load(sound_data)
        pygame.mixer.music.play()

        print("Playing sound...")
        while pygame.mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Error: {e}")

# === Manual Update Function ===

def manual_update():
    update_available, latest_version, latest_build_info = check_for_update()

    if update_available:
        print(f"🔄 New version {latest_version} is available!")
        update_script()  # Update the script
        # No need to save version info locally, just restart with the updated script
        restart_script()  # Restart the script with the updated version
    else:
        # Correctly display the local version (__version__) rather than default 0.0
        print(f"✅ You are on the latest version {__version__}.")
        
        # Fetching build details from the 'build_info' section of vs_info.json
        build_info = latest_build_info.get("build_info", {})
        build_date = build_info.get('build_date', 'N/A')
        last_updated = build_info.get('updated_on', 'N/A')
        required_packages = build_info.get('required_packages', [])

        print(f"Build Date: {build_date}")
        print(f"Last Updated: {last_updated}")
        print(f"Required Packages: {', '.join(required_packages) if required_packages else 'None'}")

# === Main ===

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Select option (1-5): ")

        if choice == "1":
            show_guns()
        elif choice == "2":
            show_tiktok()
        elif choice == "3":
            play_sound_from_url(SOUND_URL)
        elif choice == "4":
            manual_update()  # Call the manual update function
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
