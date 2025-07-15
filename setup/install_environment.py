import subprocess
import sys

def main():
    print("🔧 Setting up your Buyers Presentation Tool environment...")

    # Check if we're running inside PyInstaller EXE
    if getattr(sys, 'frozen', False):
        print("🚀 Running from EXE - skipping pip install to avoid recursion.")
    else:
        print("🚀 Installing all required packages from requirements.txt")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("\n🎉 All set! You can now run your dashboard using the separate launcher.")
        except subprocess.CalledProcessError as e:
            print("❌ Something went wrong during installation.")
            print(e)

if __name__ == "__main__":
    main()
