from processor import *
from print_logo import *
import os 
print_logo()

PARSER = 'Cites'

DATA_DIR = "C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA"
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA/Data_To_Process/'+ PARSER)
LIST_ID = os.listdir()
# let's split the list in 10 parts to reduce the risk of running out of memory and accelerate the process
# We save the data of each json into a dict which is slow if the dict is too big
LIST_ID = [LIST_ID[i:i + int(len(LIST_ID)/10)] for i in range(0, len(LIST_ID), int(len(LIST_ID)/10))]
def merge_csv (parser, data_dir, part):
    import pandas as pd 
    import os 
    os.chdir(data_dir + '/Data_To_Process/'+ parser)
    df = pd.DataFrame()
    for i in range(part):
        df = pd.concat([df, pd.read_csv('data_part_{}.csv'.format(i))], axis=0)
    df.to_csv('data.csv', index=False)


for i, l_id in enumerate(LIST_ID) :
    processor = Processor(Parser = PARSER, tag=None,  data_dir=DATA_DIR , subfolder = None, part= i)
    processor.process_and_write_csv(l_id)
    print('part {} done'.format(i))
    
merge_csv(PARSER, DATA_DIR, len(LIST_ID))




