
import os,subprocess

try:
    import fichub_cli
except ImportError as e:
    print(f"Error: {e}. Ensure fichub_cli is installed with 'pip install -U fichub-cli'")



INPUT_DIR = "Input"
OUTPUT_DIR = "Output"

class Downloader:
    def __init__(self):
        self.test = "test"
        

        #setup checks
        if not os.path.exists(INPUT_DIR):
            print(f"Input directory, {INPUT_DIR}, doesnt exist!\nCreating!...\n")
            os.mkdir(INPUT_DIR)
            with open(os.path.join(INPUT_DIR,"infile.txt"), "w") as file:
                file.write("# Please enter the URL of each story as a new line.")
            
        if not os.path.exists(OUTPUT_DIR):
            print(f"Output directory, {OUTPUT_DIR}, doesnt exist!\nCreating!...\n")
            os.mkdir(OUTPUT_DIR)
    
    #download one story
    def download(self, url, format):
        subprocess.run(['fichub_cli', '-o', OUTPUT_DIR, '-u', url, '--format',format], check=True)
        print(f'Story downloaded to {OUTPUT_DIR}')


    #bulk download
    def download_from_file(self,file,format):
        return
    
    
downloader = Downloader()
downloader.download("https://www.fanfiction.net/s/12806645/1/All-Dogs-Go-To-Valhalla","PDF")
    

