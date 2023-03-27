# %%
import os 
from datetime import datetime
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI')
from Dowloander_List_ID import *
from print_logo import *

print_logo()
DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"  
# open the file and read the content in a list
with open(DATA_DIR+'/list_of_venue_C73484699.txt', 'r') as infile:
    LIST_VENUE_ID = infile.readlines()
LIST_VENUE_ID = [x.strip() for x in LIST_VENUE_ID]


OWERWRITE = False
PAPER_API = {
    'name': "Paper",
    'path': "https://api.openalex.org/works?filter=host_venue.id:",
    'content': 'Paper metadata'
}

def download_api(api, ID):
    print("download API {} ".format(api['name']))
    downloader = Downloader(api, ID, DATA_DIR,
                            overwrite=OWERWRITE, delay=0)
    tnow = datetime.now()
    print ("start download API {} / {}".format(api['name'], str(tnow)))
    downloader.download()
    print("done in {}".format(datetime.now() - tnow))
    
for venues in LIST_VENUE_ID :
    now = datetime.now()
    download_api(PAPER_API, venues)
    print("done in {}".format(datetime.now() - now))

# %%
