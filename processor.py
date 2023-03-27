import os
os.chdir('C:/Users/ahoussard/Documents/Python_Scripts/OpenAlexAPI')
import json 
from parse_paper import PaperParser
from parse_citation import ParseCitation
import pandas as pd

class Processor:
    def __init__(self, Parser  , data_dir="./data" , subfolder = None  , tag = None ,conept_id = None , part = None):
        self.data_dir = data_dir
        self.tag = tag
        if Parser == 'Cited' or Parser == 'Cites' or Parser == 'Works':
            self.parser = ParseCitation(file_name=id ,tag = self.tag  )
            self.api_name = Parser
            self.subfolder = subfolder
            self.part = part
        elif Parser == 'Paper':
            self.parser = PaperParser()
            self.api_name = Parser
            self.subfolder = subfolder
        

    def build_path(self):
        basedir = self.data_dir+'/Data_To_Process/'+self.api_name
        return basedir 
    
    def read_json(self, id ):
        basedir = self.build_path()
        if self.tag is not None :
            outpath = basedir+ '/'+  self.tag  +'/'+ str(id) +'/' +str(id)+'.json'
        elif self.subfolder is not None:
            outpath = basedir+'/'+self.subfolder + '/' + str(id) + '/' + str(id)+'.json'        
        else : 
            outpath = basedir+ '/' + str(id) +'/' +str(id)+'.json'

        with open(outpath, 'r') as infile:
            data = json.load(infile)
        print('\t read from {}'.format(outpath))
        
        return data
    
    def process(self, parser , id ):
        data = self.read_json(id )
        print('\t process {}'.format(id))
        data_parsed = parser.parse_data(data)
        return data_parsed
    
    def process_list(self, list_id ):
        print('\t process {} list_id'.format(len(list_id)))
        data_parsed = []
        for ids in list_id:
                data_parsed.append(self.process(self.parser, ids ))
        return data_parsed

    def process_list_dict_style(self, list_id ):
        print('\t process {} list_id'.format(len(list_id)))
        data_parsed = []
        for  ids in list_id:
                data = self.process(self.parser, ids )
                for items in data:
                    items['ID_Referenceur'] = ids
                    data_parsed.append(items)
        return data_parsed

    def process_and_write_csv(self, list_id):
        if self.api_name == 'Cites' or self.api_name == 'Cited' or self.api_name == 'Works':
            data = self.process_list_dict_style(list_id)
        else :
            data = self.process_list(list_id)
        if self.subfolder is not None:
            outpath = self.data_dir+'/' +str(self.api_name)+'_'+str(self.subfolder)+'.csv'
        if self.part is not None :
            outpath = self.data_dir+'/' +str(self.api_name)+'_'+str(self.part)+'.csv'
        else : 
            outpath = self.data_dir+'/' +str(self.api_name)+'.csv'
        dataframe = pd.DataFrame(data)
        dataframe.to_csv(outpath, index=False, sep=';')  
        print('\t write to {}'.format(outpath))
    