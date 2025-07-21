import subprocess
import sys
import os

REQUIREMENTS_FILE = "requirements.txt"

def install_requirements():
    print("📦 Installing required Python packages...\n")

    if not os.path.exists(REQUIREMENTS_FILE):
        print(f"❌ Missing {REQUIREMENTS_FILE} in the current directory.")
        sys.exit(1)

    try:
        subprocess.run(["python", "-m", "pip", "install", "-r", REQUIREMENTS_FILE], check=True)
        print("\n✅ All packages installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Package installation failed:\n{e}")
        sys.exit(1)

def main():
    print("🔍 Checking if Python is available...")

    try:
        subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT)
    except Exception:
        print("❌ Python not found in PATH. Please install it first.")
        sys.exit(1)

    install_requirements()

    print("\n🎉 Requirements setup complete. You’re ready to run the app.")

if __name__ == "__main__":
    main()

