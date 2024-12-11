
import os,subprocess
from time import sleep

import shutil

try:
    import fichub_cli
except ImportError as e:
    print("f'Error: {e}. Ensure fichub_cli is installed with 'pip install -U fichub-cli'")



INPUT_DIR = 'Input'
OUTPUT_DIR = 'Output'

DOWNLOAD_FORMAT ="PDF"

class Downloader:
    def __init__(self):
        self.test = 'test'
        

        #setup checks
        if not os.path.exists(INPUT_DIR):
            print(f'Input directory, {INPUT_DIR}, doesnt exist!\nCreating!...\n')
            os.mkdir(INPUT_DIR)
            with open(os.path.join(INPUT_DIR,'infile.txt'), 'w') as file:
                file.write('# Please enter the URL of each story as a new line.\n')
            
        if not os.path.exists(OUTPUT_DIR):
            print(f'Output directory, {OUTPUT_DIR}, doesnt exist!\nCreating!...\n')
            os.mkdir(OUTPUT_DIR)
    
    #download one story
    def download(self, url, format):
        subprocess.run(['fichub_cli', '-o', OUTPUT_DIR, '-u', url, '--format',format], check=True)
        print(f'Story downloaded to {OUTPUT_DIR}')


    #bulk download from infile
    def download_from_file(self,file,format):

        command_str = ''

        with open(os.path.join(INPUT_DIR,file), 'r') as in_file:
            
            lines = [line.strip() for line in in_file.readlines()]
            
            if(lines[0] == '# Please enter the URL of each story as a new line.'):
                lines.pop(0)
            
        

        for line in lines:
            command_str += line + ','
        command_str = command_str.removesuffix(',')

    
        print(command_str)
        return
        subprocess.run(['fichub_cli', '-o', OUTPUT_DIR, '-l', fileList, '--format',format], check=True)
        print(f'Story downloaded to {OUTPUT_DIR}')
        return
    
    def menu_settings(self):
            os.system('cls||clear')
            print('╔═════════════════════════════════════════════════╗')
            print('║                   Settings Menu                 ║')
            print('╟─────────────────────────────────────────────────╢')
            print('║ [1] - Change Download format                    ║')
            print('║ [2] - Rebuild Input/Output directories          ║')
            print('║ [3] - Back to Main Menu                         ║')
            print('╚═════════════════════════════════════════════════╝')
            user_input = input('Please select an option (1-4). \nSelection: ').strip()
            if(user_input == '1'):
                

                self.menu_single_download()
            elif(user_input == '2'):
                while True:
                    print(f'\nYou entered: Rebuild Input/Output directories \n')
                    print('WARNING: This is potentially destructive and will delete and recreate the input and output directories. \nALL existing data will be lost!')
                    sleep(3)
                    confirm = input('\nProceed? (Y/n):').strip().lower()
                    if(confirm == 'y' or confirm == 'yes'):
                        print('Rebuilding...')
                        shutil.rmtree(INPUT_DIR, ignore_errors=True)
                        os.mkdir(INPUT_DIR)
                        with open(os.path.join(INPUT_DIR,'infile.txt'), 'w') as file:
                            file.write('# Please enter the URL of each story as a new line.\n')
                        print("Rebuilt input directory...")
                        sleep(1)
                        print(f'Output directory, {OUTPUT_DIR}, doesnt exist!\nCreating!...\n')
                        shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
                        os.mkdir(OUTPUT_DIR)
                        print("Rebuilt output directory...")
                        sleep(1.5)
                        return

                    elif(confirm == 'n' or confirm == 'no'):
                        print('Aborting!')
                        return
                    else:
                        print("Error: unknown input!\nAborting!\n")
                        sleep(1)
                        return
            elif(user_input == '3'):
                return
            
            else: 
                print('Error! Invalid choice!')

    def basic_url_check(self,url):
        if 'fanfiction.net' in url:
            return True
        else:
            return False

    def menu_single_download(self):
        os.system('cls||clear')
        while True:
            os.system('cls||clear')
            print('╔═════════════════════════════════════════════════╗')
            print('║              Download Single Story              ║')
            print('╟─────────────────────────────────────────────────╢')
            print(f'╟-Format:          {DOWNLOAD_FORMAT.ljust(31)}║')
            print(f'╟-Output Location: {OUTPUT_DIR.ljust(31)}║')
            print('╟─────────────────────────────────────────────────╢')
            print("║ Type 'menu' to return to the main menu.         ║")
            print('╚═════════════════════════════════════════════════╝')
            url = input('Enter the URL to the story\nURL: ').strip()
            
            if(url.lower() == 'menu'):
                return()
            
            
            #confirm it
            while True:
                
                print(f'\nYou entered: {url.lower()}\n')
                confirm = input('Proceed with download? (Y/n):').strip().lower()
                if(confirm == 'y' or confirm == 'yes'):
                    print('Downloading...')
                    
                    self.download(url.lower(),DOWNLOAD_FORMAT)
                    return

                elif(confirm == 'n' or confirm == 'no'):
                    print('Aborting!')
                    break
                else:
                    print("Error: unknown input!\nPlease enter 'yes' or 'no'\n")
                    sleep(1)
                    continue


    def menu_bulk_download(self): 

        with open(os.path.join(INPUT_DIR,"infile.txt"), 'r') as in_file:
            
            lines = [line.strip() for line in in_file.readlines()]
            
            if(lines[0] == '# Please enter the URL of each story as a new line.'):
                lines.pop(0)


        os.system('cls||clear')
        while True:
            print('╔═════════════════════════════════════════════════╗')
            print('║             Download Muliple Stories            ║')
            print('╟─────────────────────────────────────────────────╢')
            
            print(f'╟ Format: {DOWNLOAD_FORMAT.ljust(40)}║')
            print(f'╟ Input File: {INPUT_DIR}/infile.txt'.ljust(50) + '║')
            print(f'╟ Output Location: {OUTPUT_DIR.ljust(31)}║')
            print('╟─────────────────────────────────────────────────╢')
            
            print(f"║Found {len(lines)} entries in 'infile.txt'".ljust(50) + "║" + "\n║Type 'menu' to return to the main menu.          ║")
            print('╚═════════════════════════════════════════════════╝')
            uinput = input("Press Enter to start downloading or type 'switch' to use a different file. \nCommand: ").strip().lower()
            if uinput == 'menu':
                return
            elif uinput == 'switch':
                infile = input('\nPlease enter the full name of the file to you would like to read from.\nFilename: ')
                while True:
                    print('╔═════════════════════════════════════════════════╗')
                    print('║             Download Muliple Stories            ║')
                    print('╟─────────────────────────────────────────────────╢')
                    
                    print(f'╟ Format: {DOWNLOAD_FORMAT.ljust(40)}║')
                    print(f'╟ Input File: {INPUT_DIR}/{infile}'.ljust(50) + '║')
                    print(f'╟ Output Location: {OUTPUT_DIR.ljust(31)}║')
                    print('╟─────────────────────────────────────────────────╢')
                    
                    print(f"║Found {len(lines)} entries in 'infile.txt'".ljust(50) + "║" + "\n║Type 'menu' to return to the main menu.          ║")
                    print('╚═════════════════════════════════════════════════╝')
                    uinput = input("Press Enter to start downloading.\nCommand: ").strip().lower()
                    if uinput == 'menu':
                        return
                    else:
                        self.download_from_file(os.path.join(INPUT_DIR,infile))
                        return()
            else:
                self.download_from_file(os.path.join(INPUT_DIR,'infile.txt'))

    def menu(self):
        while True:
            
            os.system('cls||clear')
            print('╔═════════════════════════════════════════════════╗')
            print('║                    Main Menu                    ║')
            print('╟─────────────────────────────────────────────────╢')
            print('║ [1] - Download single story                     ║')
            print('║ [2] - Download multiple stories from a file     ║')
            print('║ [3] - Settings                                  ║')
            print('║ [4] - Quit                                      ║')
            print('╚═════════════════════════════════════════════════╝')

            user_input = input('Please select an option (1-4). \nSelection: ').strip()
            if(user_input == '1'):
                

                self.menu_single_download()
            elif(user_input == '2'):
                self.menu_bulk_download()
            elif(user_input == '3'):
                self.menu_settings()
            elif(user_input == '4'):
                return
            else: 
                print('Error! Invalid choice!')
                 
                
            
            


downloader = Downloader()



downloader.menu()


