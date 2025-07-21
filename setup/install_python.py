import subprocess
import sys
import os

MIN_VERSION = (3, 10)
INSTALLER_FILE = "python-3.13.5-amd64.exe"  # Update this if using a different version

def is_python_installed(min_version=MIN_VERSION):
    try:
        output = subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT)
        version_str = output.decode().strip().split()[-1]
        major, minor, *_ = map(int, version_str.split("."))
        return (major, minor) >= min_version
    except Exception:
        return False

def run_python_installer():
    installer_path = os.path.join(os.path.dirname(__file__), INSTALLER_FILE)
    if not os.path.exists(installer_path):
        print(f"❌ Installer not found: {installer_path}")
        return

    print(f"📦 Launching Python installer: {INSTALLER_FILE}")
    subprocess.run([installer_path])
    print("ℹ️ Installer closed. You may need to restart your terminal or PC for the install to take effect.")

def main():
    print("🔧 Checking for Python installation...")

    if is_python_installed():
        print("✅ Python is already installed and meets the version requirement.")
    else:
        print("🚫 Python not found or version is outdated.")
        run_python_installer()

if __name__ == "__main__":
    main()
