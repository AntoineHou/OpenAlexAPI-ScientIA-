import pandas as pd

class ParseCitation () :
    
    def __init__ (self, file_name , tag) :
        self.keys = ['id' ,'author', 'date', 'referenced_works' , 'cited_by_count', 'venue' , 'venue_type', 
        'concepts', 'concepts_values', 'fields_of_study','abstract']
        self.focal_node = file_name
        self.tag = tag
        self.compteur = 0
        self.field_dict = pd.read_csv('C:/Users/ahoussard/Documents/Data_mag/papersMAGWOS/WOS_MAG_journals.csv', sep = ',', encoding = 'utf-8' , index_col=['MAG_journal_Id'])
        self.field_dict = self.field_dict[~self.field_dict.index.duplicated(keep='first')]
        self.field_dict = self.field_dict['Web of Science Categories'].to_dict()

    def value_is_none (self , value) : 
        if value == None : 
            return True 
    
    def check_file(self ,dict_from_json ) : 
        if len(dict_from_json) != 0 : 
            return True 
        else :
            return False
    
    def abstract_dict_to_string (self , abstract_dict ) :
        try : 
            NB_CHAR = max([sublist[-1] for sublist in list(abstract_dict.values())])
            abstract_string = ['.' for i in range(NB_CHAR+1)]
            for key , value in abstract_dict.items() : 
                for items in value : 
                    if "$" in key :
                        abstract_string[items] = "LATEX"
                    else :
                        abstract_string[items] = str(key+' ')
            return ''.join(abstract_string)
        except ValueError : 
            return None
    
    def parse_abstract (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['results'][self.compteur]['abstract_inverted_index']) : 
                    return None
                else : 
                    return self.abstract_dict_to_string(dict_from_json['results'][self.compteur]['abstract_inverted_index'])
            except KeyError : 
                return None
        else : 
            return None
    
    def parse_authors (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                authors = []
                for items in dict_from_json['results'][self.compteur]['authorships'] : 
                    if self.value_is_none(items) : 
                        pass
                    else : 
                        authors.append(items['author']['id'].split('.org/')[1])
                return authors
            except  : 
                return None
        else :
            return None
    
    def parse_date (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) : 
            try : 
                if self.value_is_none(dict_from_json['results'][self.compteur]['publication_date']) : 
                    return None
                else : 
                    return str(dict_from_json['results'][self.compteur]['publication_date'])
            except  : 
                return None
        else : 
            return None

    def parse_n_citation (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                if self.value_is_none(dict_from_json['results'][self.compteur]['cited_by_count']) : 
                    return None
                else : 
                    return dict_from_json['results'][self.compteur]['cited_by_count']
            except  : 
                return None
        else :
            return None
    
    def parse_biblio (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                biblio = []
                for items in dict_from_json['results'][self.compteur]['referenced_works'] : 
                    if self.value_is_none(items) : 
                        pass
                    else : 
                        biblio.append(items.split('.org/')[1])
                return biblio
            except  : 
                return None
        else :
            return None
    
    def parse_concepts (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                concepts = []
                for items in dict_from_json['results'][self.compteur]['concepts'] : 
                    if self.value_is_none(items) : 
                        pass
                    elif float(items['score']) > 0.05 : 
                        concepts.append(items['id'].split('.org/')[1])
                    else :
                        pass
                return concepts
            except  : 
                return None
        else :
            return None
    
    def parse_concepts_values (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                concepts_values = [] 
                for items in dict_from_json['results'][self.compteur]['concepts'] : 
                    if self.value_is_none(items) : 
                        pass
                    elif float(items['score']) > 0.05 : 
                        concepts_values.append(float(items['score']))
                    else :
                        pass
                return concepts_values 
            except  : 
                return None
        else :
            return None
    

    def parse_venue_id (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                if self.value_is_none(dict_from_json['results'][self.compteur]['host_venue']['id']) : 
                    return None
                else : 
                    return dict_from_json['results'][self.compteur]['host_venue']['id'].split('.org/')[1]
            except  : 
                return None
        else :
            return None
    
    def parse_venue_type (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                if self.value_is_none(dict_from_json['results'][self.compteur]['host_venue']['type']) : 
                    return None
                else : 
                    return dict_from_json['results'][self.compteur]['host_venue']['type']
            except  : 
                return None
        else :
            return None

    def parse_venue (self , dict_from_json ) :
        return self.parse_venue_id(dict_from_json) , self.parse_venue_type(dict_from_json)
        


    def parse_field_of_study (self, dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                if int(dict_from_json['results'][self.compteur]['host_venue']['id'].split('.org/')[1][1:]) in self.field_dict.keys() : 
                    return self.field_dict[int(dict_from_json['results'][self.compteur]['host_venue']['id'].split('.org/')[1][1:])]
                else :
                    return None
            except  :
                return None
        else :
            return None
    
    def parse_id (self , dict_from_json ) :
        if self.check_file(dict_from_json['results'][self.compteur]) :
            try : 
                return dict_from_json['results'][self.compteur]['id'].split('.org/')[1]
            except  : 
                return None
        else :
            return None

    def parse_data (self , dict_from_json ) :
        DICTS = []
        for i in range(len(dict_from_json['results'])) :
            Venue , Type = self.parse_venue(dict_from_json)
            DICTS.append({'id' : self.parse_id(dict_from_json) ,
            self.keys[0] : self.parse_id(dict_from_json) , 
            self.keys[1] : self.parse_authors(dict_from_json) , 
            self.keys[2] : self.parse_date(dict_from_json) , 
            self.keys[3] : self.parse_biblio(dict_from_json) , 
            self.keys[4] : self.parse_n_citation(dict_from_json) , 
            self.keys[5] : Venue, 
            self.keys[6] : Type ,
            self.keys[7] : self.parse_concepts(dict_from_json) , 
            self.keys[8] : self.parse_concepts_values(dict_from_json),
            self.keys[9] : self.parse_field_of_study(dict_from_json),
            self.keys[10] : self.parse_abstract(dict_from_json) })
            self.compteur = self.compteur+1
        self.compteur = 0
        return DICTS
