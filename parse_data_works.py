from processor import *
from print_logo import *
import os 

print_logo()

PARSER = 'Works'
TAG = 'C188147891'
DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"  
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA/download/Works'+'/'+TAG) 
LIST_ID = os.listdir()
processor = Processor(Parser = PARSER, tag=TAG,  data_dir=DATA_DIR , subfolder = None )
processor.process_and_write_csv(LIST_ID)

