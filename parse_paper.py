from typing import Any
import pandas as pd
class PaperParser:

    def __init__ (self ) -> None :
        self.keys = ['id' , 'title' , 'date' ,  'authors' , 'n_citation' , 'biblio', 'concepts' , 'concepts_value',
        'venue' , 'type' , 'abstract' ]
        self.field_dict = pd.read_csv('C:/Users/ahoussard/Documents/Data_mag/papersMAGWOS/WOS_MAG_journals.csv', sep = ',', encoding = 'utf-8' , index_col=['MAG_journal_Id'])
        self.field_dict = self.field_dict[~self.field_dict.index.duplicated(keep='first')]
        self.field_dict = self.field_dict['Web of Science Categories'].to_dict()

    def value_is_none (self , value) : 
        if value == None : 
            return True 
    
    def check_file(self ,dict_from_json ) : 
        if len(dict_from_json) != 0 : 
            return True 

    def parse_id (self , dict_from_json ) : 
        if self.check_file(dict_from_json) : 
            try :
                if self.value_is_none(dict_from_json['id']) : 
                    return None
                else : 
                    return dict_from_json['id'].split('.org/')[1]
            except KeyError : 
                return None
        else : 
            return None
    
    def parse_title (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['title']) : 
                    return None
                else : 
                    return dict_from_json['title']
            except KeyError : 
                return None
        else : 
            return None
    
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
                if self.value_is_none(dict_from_json['abstract_inverted_index']) : 

                    return None
                else : 
                    return self.abstract_dict_to_string(dict_from_json['abstract_inverted_index'])
        else : 
            return None
    
    def parse_date (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['publication_date']) : 
                    return None
                else : 
                    return str(dict_from_json['publication_date'])
            except KeyError : 
                return None
        else : 
            return None

    def parse_authors (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                authors = []
                for items in dict_from_json['authorships'] : 
                    if self.value_is_none(items) : 
                        pass
                    else : 
                        authors.append(items['author']['id'].split('.org/')[1])
                return authors
            except KeyError : 
                return None
        else :
            return None
    
    def parse_n_citation (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                if self.value_is_none(dict_from_json['cited_by_count']) : 
                    return None
                else : 
                    return dict_from_json['cited_by_count']
            except KeyError : 
                return None
        else :
            return None
    
    def parse_biblio (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
                biblio = []
                for items in dict_from_json['referenced_works'] : 
                    if self.value_is_none(items) : 
                        pass
                    else : 
                        biblio.append(items.split('.org/')[1])
                return biblio

        else :
            return None

    def parse_concepts (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                concepts = []
                for items in dict_from_json['concepts'] : 
                    if self.value_is_none(items) : 
                        pass
                    elif float(items['score']) > 0.05  : 
                        concepts.append(items['id'].split('.org/')[1])
                    else :
                        pass
                return concepts
            except KeyError : 
                return None
        else :
            return None
    
    def parse_concepts_value (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                concepts_value = []
                for items in dict_from_json['concepts'] : 
                    if self.value_is_none(items) : 
                        pass
                    elif float(items['score']) > 0.05  : 
                        concepts_value.append(float(items['score']))
                    else :
                        pass
                return concepts_value
            except KeyError : 
                return None
        else :
            return None
    
    def parse_venue (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                if self.value_is_none(dict_from_json['host_venue']['id']) : 
                    Venue_ID = None  
                else :
                    Venue_ID = dict_from_json['host_venue']['id'].split('.org/')[1]
                if self.value_is_none(dict_from_json['host_venue']['type']) : 
                    Type = None
                else :  
                    Type = dict_from_json['host_venue']['type']
                return Venue_ID , Type
            except KeyError : 
                return None ,None
        else :
            return None , None

    def parse_field_of_study (self, dict_from_json ) :
        if self.check_file(dict_from_json) :
            try : 
                if int(dict_from_json['host_venue']['id'].split('.org/')[1][1:]) in self.field_dict.keys() : 
                    return self.field_dict[int(dict_from_json['host_venue']['id'].split('.org/')[1][1:])]
                else :
                    return None
            except  :
                return None
        else :
            return None

    def parse_paper (self , dict_from_json) :
        if self.check_file(dict_from_json)   :
            paper = {}
            paper['id'] = self.parse_id(dict_from_json)
            paper['title'] = self.parse_title(dict_from_json)
            paper['date'] = self.parse_date(dict_from_json)
            paper['authors'] = self.parse_authors(dict_from_json)
            paper['n_citation'] = self.parse_n_citation(dict_from_json)
            paper['biblio'] = self.parse_biblio(dict_from_json)
            paper['concepts'] = self.parse_concepts(dict_from_json)
            paper['concepts_value'] = self.parse_concepts_value(dict_from_json)
            Venue , Type = self.parse_venue(dict_from_json)
            paper['venue'] = Venue
            paper['type'] = Type
            paper['abstract'] = self.parse_abstract(dict_from_json)
            paper['field'] = self.parse_field_of_study(dict_from_json)
            return paper
        else :
            return None

    def parse_data (self , dict_from_json ) -> Any :
        return self.parse_paper(dict_from_json  )
                






