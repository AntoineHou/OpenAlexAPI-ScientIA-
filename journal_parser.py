class ParseJournal ():

    def __init__ (self) -> None :
        self.keys = ['id' , 'display_name' , 'cited_by_count' ,  'works_count' ,'activity' , 'country_code' ]

    def check_file(self ,dict_from_json ) : 
        if len(dict_from_json) != 0 : 
            return True 
    
    def value_is_none (self , value) : 
        if value == None : 
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
    
    def parse_display_name (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['display_name']) : 
                    return None
                else : 
                    return dict_from_json['display_name']
            except KeyError : 
                return None
        else : 
            return None
    
    def parse_cited_by_count (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['cited_by_count']) : 
                    return None
                else : 
                    return str(dict_from_json['cited_by_count'])
            except KeyError : 
                return None
        else : 
            return None
    
    def parse_works_count (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['works_count']) : 
                    return None
                else : 
                    return str(dict_from_json['works_count'])
            except KeyError : 
                return None
        else : 
            return None
    
    def parse_activity (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['counts_by_year']) : 
                    return None
                else : 
                    D = {}
                    for i in len(dict_from_json['counts_by_year']) : 
                        D[dict_from_json['counts_by_year'][i]['year']] = {'works_count' : dict_from_json['counts_by_year'][i]['works_count'] , 'cited_by_count' : dict_from_json['counts_by_year'][i]['cited_by_count']}
                    return D
            except KeyError :   
                return None
        else : 
            return None
    
    def parse_country_code (self , dict_from_json ) :
        if self.check_file(dict_from_json) : 
            try : 
                if self.value_is_none(dict_from_json['country_code']) : 
                    return None
                else : 
                    return dict_from_json['country_code']
            except KeyError : 
                return None
        else : 
            return None

    def parse_journal (self , dict_from_json) :
        if self.check_file(dict_from_json) :
            journal = {}
            journal['id'] = self.parse_id(dict_from_json)
            journal['display_name'] = self.parse_display_name(dict_from_json)
            journal['cited_by_count'] = self.parse_cited_by_count(dict_from_json)
            journal['works_count'] = self.parse_works_count(dict_from_json)
            journal['activity'] = self.parse_activity(dict_from_json)
            journal['country_code'] = self.parse_country_code(dict_from_json)
            return journal
        else :
            return None

    def parse_data (self , dict_from_json ) -> Any :
        return self.parse_journal(dict_from_json  )