import os
import platform
import webbrowser
import requests
import pygame
from io import BytesIO

# === CONFIG ===
GUNS_USERNAME = "vexi.tech"
TIKTOK_USERNAME = "@v3x1.tech"
SOUND_URL = "https://raw.githubusercontent.com/VexisTheFox/vexi-script/main/rawr.mp3"  # update this

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def show_menu():
    print("=== Terminal Tool ===")
    print("1. Show my guns.lol")
    print("2. Show my TikTok")
    print("3. Play Rawr")
    print("4. Exit")

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

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Select option (1-4): ")

        if choice == "1":
            show_guns()
        elif choice == "2":
            show_tiktok()
        elif choice == "3":
            play_sound_from_url(SOUND_URL)
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
