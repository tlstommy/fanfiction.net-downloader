
import os,subprocess

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
                file.write('# Please enter the URL of each story as a new line.')
            
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
        print('menu settings here')

    def menu_single_download(self):
        os.system('cls||clear')
        while True:
            print('╔════════════════════════════')
            print('║Download Single Story')
            print(f'╟Format: {DOWNLOAD_FORMAT}')
            print(f'╟Output Location: {OUTPUT_DIR}')
            print("║Please enter the URl of the story below. \n║Type 'menu' to return to the main menu.")
            print('║═══════════════════════════')
            print('╚════════════════════════════')
            url = input('Story URL: ').strip()
            
            if(url.lower() == 'menu'):
                return()
            
            #confirm it
            while True:
                print(f'\nYou entered: {url.lower()}\n')
                confirm = input('Proceed with download? (Y/n):').strip().lower()
                if(confirm == 'y' or confirm == 'yes'):
                    print('Downloading...')
                    self.download(url.lower(),DOWNLOAD_FORMAT)

                elif(confirm == 'n' or confirm == 'no'):
                    print('Aborting!')
                    break
                else:
                    print("Error: unknown input!\nPlease enter 'yes' or 'no'\n")
                    continue


    def menu_bulk_download(self): 

        with open(os.path.join(INPUT_DIR,"infile.txt"), 'r') as in_file:
            
            lines = [line.strip() for line in in_file.readlines()]
            
            if(lines[0] == '# Please enter the URL of each story as a new line.'):
                lines.pop(0)


        os.system('cls||clear')
        while True:
            print('╔════════════════════════════')
            print('║Download multiple stories')
            print(f'╟Format: {DOWNLOAD_FORMAT}')
            print(f'╟Input File: {INPUT_DIR}/infile.txt')
            print(f'╟Output Location: {OUTPUT_DIR}')
            print(f"║Found {len(lines)} entries in 'infile.txt' \n║Type 'menu' to return to the main menu.")
            
            print('╚════════════════════════════')
            uinput = input("Press enter to contine. If you would like to use a diffrent file, type 'switch'.\n ").strip()
            
            if(uinput.lower() == 'menu'):
                return()
            
            if(uinput.lower() == 'switch'):
                return()
            
            #confirm it
            while True:

    def menu(self):
        while True:
            
            os.system('cls||clear')
            print('--------------------------------')
            print('What would you like to do?')
            print('[1] - Download a single story')
            print('[2] - Download multiple stories from a file')
            print('[3] - Settings')
            print('[4] - Quit')

            user_input = input('Please select an option (1-4): ').strip()
            if(user_input == '1'):
                

                self.menu_single_download()
            elif(user_input == '2'):
                self.menu_bulk_download
            elif(user_input == '3'):
                self.menu_settings()
            elif(user_input == '4'):
                return
            else: 
                print('Error! Invalid choice!')
                 
                
            
            


downloader = Downloader()
#downloader.download('https://www.fanfiction.net/s/12806645/1/All-Dogs-Go-To-Valhalla','PDF')


downloader.menu()


