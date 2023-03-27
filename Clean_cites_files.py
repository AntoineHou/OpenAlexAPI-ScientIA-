import os 
import json
#c524765639
DATA_DIR = 'C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI/DATA/Data_To_Process/Cites'
FOLDERS = os.listdir(DATA_DIR)


for folder in FOLDERS:
    FILES = os.listdir(DATA_DIR+'/'+folder)
    print('processing folder {}'.format(folder))
    if len(FILES) == 1:
        os.rename(DATA_DIR+'/'+folder+'/'+FILES[0], DATA_DIR+'/'+folder+'/'+folder+'.json')
    elif len(FILES) > 1: 
        data = {}
        for i , file in enumerate(FILES):
                if i == 0:
                    with open(DATA_DIR+'/'+folder+'/'+file, 'r') as infile:
                        d = json.load(infile)
                    data.update(d)
                    os.remove(DATA_DIR+'/'+folder+'/'+file)
                else :
                    with open(DATA_DIR+'/'+folder+'/'+file, 'r') as infile:
                        d = json.load(infile)
                    if 'results' in d.keys():
                        data['results'].extend(d['results'])
                        os.remove(DATA_DIR+'/'+folder+'/'+file)
                    else :
                        pass 
        with open(DATA_DIR+'/'+folder+'/'+folder+'.json', 'w') as outfile:
            json.dump(data, outfile)
    elif len(FILES) == 0 : 
        print('Folder {} is empty'.format(folder))



