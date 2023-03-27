import os 
from datetime import datetime
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA')
import Downloader_Pages
from print_logo import *
from multiprocessing import Pool
print_logo()

DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"  
LIST_YEAR = [list(range(1980,1997,1) ), list(range(1997,2007,1) ), list(range(2007,2015,1) ), list(range(2015,2020,1) )]
OWERWRITE = False
FILTERS_BASE =',publication_year:{},is_retracted:false,has_doi:true,has_references:true'
CONCEPT = 'C188147891'

# C34974158

WORKS_API = {
    'name': "Works", 
    'path': "https://api.openalex.org/works?filter=concepts.id:",
    'content': 'PAPER_METADATA',
    'filter' : False
}

def download_api(api,  DATA_DIR ,id ,sub_path=None) :
    downloader = Downloader_Pages.Downloader(api, sub_path,  DATA_DIR,
                            overwrite=OWERWRITE, delay=0)
    tnow = datetime.now()
    print ("start download API {} / {}".format(api['name'], str(tnow)))
    downloader.download(id)
    print("done in {}".format(datetime.now() - tnow))


def download_all_dates(LIST_YEAR ) :   
    now = datetime.now()
    for ID in LIST_YEAR :
        FILTERS = FILTERS_BASE.format(str(ID))
        WORKS_API['filter'] = FILTERS
        print("download cites {} ".format(str(ID)))
        download_api(WORKS_API, DATA_DIR , CONCEPT ,sub_path=str(ID))
    print("done in {}".format(datetime.now() - now))

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(download_all_dates, [LIST_YEAR[0],LIST_YEAR[1],LIST_YEAR[2],LIST_YEAR[3]])
    pool.close()
    pool.join()


