import os 
from datetime import datetime
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA')
import Downloader_Pages
from print_logo import *
from multiprocessing import Pool
print_logo()

DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"  
FILE_NAME = 'Works_C188147891.txt'
with open(DATA_DIR+'/' + FILE_NAME, 'r')as filehandle:
    LIST_ID = filehandle.read().splitlines()
LIST_ID = [x.strip() for x in LIST_ID]
LIST_ID_DONE = os.listdir(os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA/download/'
                                   +'Cites'+'/'))
MISSING_ID = [x for x in LIST_ID if x not in LIST_ID_DONE]
list_id_splited = [MISSING_ID[i:i + int(len(MISSING_ID)/4)] for i in range(0, len(MISSING_ID), int(len(MISSING_ID)/4))]
print(str(len(MISSING_ID)/len(LIST_ID)*100)+'% missing')


OWERWRITE = False

CITES_API = {
    'name': "Cites",
    'path': "https://api.openalex.org/works?filter=cites:",
    'content': 'PAPER_CITATIONS',
    'filter' : False
}

CITED_API = {
    'name': "Cited",
    'path': "https://api.openalex.org/works?filter=cited_by:",
    'content': 'PAPER_REFERENCES',
    'filter' : False
}

def download_api(api,  DATA_DIR ,id ,sub_path=None) :
    downloader = Downloader_Pages.Downloader(api, sub_path,  DATA_DIR,
                            overwrite=OWERWRITE, delay=0)
    tnow = datetime.now()
    print ("start download API {} / {}".format(api['name'], str(tnow)))
    downloader.download(id)
    print("done in {}".format(datetime.now() - tnow))

def download_all_api(list_id ) :   
    now = datetime.now()
    for ID in list_id :
        print("download cites {} ".format(ID))
        download_api(CITES_API, DATA_DIR , ID)
        MISSING_ID.remove(ID)
    print("done in {}".format(datetime.now() - now))

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(download_all_api, [list_id_splited[0],list_id_splited[1],list_id_splited[2],
                                        list_id_splited[3]] )
    pool.close()
    pool.join()


