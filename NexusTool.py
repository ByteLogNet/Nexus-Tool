import ctypes
import os
import shutil
import tempfile
import time
import subprocess
import pyfiglet
import colorama
from colorama import Fore
import sys

colorama.init(autoreset=True)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    if is_admin():
        return
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f"{script} {params}", None, 1)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cleanmgr():
    try:
        subprocess.run('cleanmgr', check=True)
        print(Fore.GREEN + "Clean tool ran successfully.")
    except subprocess.CalledProcessError as e:
        print(Fore.RED + f"Clean tool failed. {e}")

def delete_temp_files():
    user_temp_dir = tempfile.gettempdir()

    if not os.path.exists(user_temp_dir):
        print(Fore.RED + f"The temporary directory does not exist: {user_temp_dir}")
        return

    def try_delete_file(file_path, retries=3, delay=1):
        for attempt in range(retries):
            try:
                os.remove(file_path)
                return
            except OSError as e:
                if e.errno == 32:
                    time.sleep(delay)
                else:
                    print(Fore.RED + f"Failed to delete file: {file_path}. Error: {e}")
                    return

    try:
        items = os.listdir(user_temp_dir)
        if not items:
            print(Fore.RED + "No files to delete in the temporary directory.")
            return

        for item in items:
            item_path = os.path.join(user_temp_dir, item)
            if os.path.isdir(item_path):
                try:
                    shutil.rmtree(item_path)
                except Exception as e:
                    print(Fore.RED + f"Failed to remove directory: {item_path}. Error: {e}")
            else:
                try_delete_file(item_path)

        print(Fore.GREEN + "Temporary folder cleaned.")
    except Exception as e:
        print(Fore.RED + f"Error deleting user temporary files: {e}")

def delete_prefetch_files():
    prefetch_dir = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'Prefetch')

    if not os.path.exists(prefetch_dir):
        print(Fore.RED + f"The prefetch directory does not exist: {prefetch_dir}")
        return

    def try_delete_file(file_path, retries=3, delay=1):
        for attempt in range(retries):
            try:
                os.remove(file_path)
                return
            except OSError as e:
                if e.errno == 32:
                    time.sleep(delay)
                else:
                    print(Fore.RED + f"Failed to delete file: {file_path}. Error: {e}")
                    return

    try:
        items = os.listdir(prefetch_dir)
        if not items:
            print(Fore.RED + "No files to delete in the prefetch directory.")
            return

        for item in items:
            item_path = os.path.join(prefetch_dir, item)
            if os.path.isdir(item_path):
                try:
                    shutil.rmtree(item_path)
                except Exception as e:
                    print(Fore.RED + f"Failed to remove directory: {item_path}. Error: {e}")
            else:
                try_delete_file(item_path)

        print(Fore.GREEN + "Prefetch folder cleaned.")
    except Exception as e:
        print(Fore.RED + f"Error deleting prefetch files: {e}")

def main():
    ascii_letters = pyfiglet.figlet_format("Nexus Tool", font="big")
    first_run = True

    if first_run:
        input(Fore.WHITE + "Press Enter to Continue...")
        first_run = False

    while True:
        clear_terminal()
        print(Fore.MAGENTA + ascii_letters)
        print(Fore.LIGHTBLUE_EX + "===> A simple cleaner for Windows <===")
        print()
        print(Fore.WHITE + "[-] What action would you like to perform?")
        print()
        print(Fore.GREEN + "[1] Delete Temp Files")
        print(Fore.GREEN + "[2] Run Cleaning Tool")
        print(Fore.GREEN + "[3] Delete Prefetch Files")
        print(Fore.GREEN + "[4] Exit")
        print()
        choice = input(Fore.WHITE + "Your Choice: ")

        if choice == '1':
            delete_temp_files()
        elif choice == '2':
            cleanmgr()
        elif choice == '3':
            delete_prefetch_files()
        elif choice == '4':
            print(Fore.GREEN + "Exiting...")
            break
        else:
            print(Fore.RED + "Invalid choice. Please enter a number between 1 and 4.")

        input(Fore.BLUE + "Press Enter to return to the menu...")

if __name__ == "__main__":
    if not is_admin():
        run_as_admin()
    else:
        main()
