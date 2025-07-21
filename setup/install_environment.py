import os
import subprocess
import sys
import shutil
import urllib.request

PYTHON_INSTALLER_URL = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
PYTHON_INSTALLER_FILE = "python_installer.exe"

def is_python_installed():
    try:
        subprocess.check_output(["python", "--version"])
        return True
    except Exception:
        return False

def download_python_installer(url, filename):
    print(f"⬇️ Downloading Python installer from {url}...")
    urllib.request.urlretrieve(url, filename)
    print("✅ Download complete.")

def launch_installer_gui(installer_path):
    print("💡 Launching Python installer GUI... Please complete the installation manually.")
    subprocess.run([installer_path])  # No `/quiet`, launches GUI
    input("🔄 Press ENTER after you've completed the Python installation...")

def main():
    print("🔧 Setting up your Buyers Presentation Tool environment...")

    if not is_python_installed():
        print("🚫 Python not found on this system.")
        if not os.path.exists(PYTHON_INSTALLER_FILE):
            download_python_installer(PYTHON_INSTALLER_URL, PYTHON_INSTALLER_FILE)
        launch_installer_gui(PYTHON_INSTALLER_FILE)

    try:
        print("🚀 Installing required packages from requirements.txt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("🎉 Setup complete!")
    except Exception as e:
        print("❌ Failed to install requirements.")
        print(e)

if __name__ == "__main__":
    main()
