class ParseConcepts () :

    def __init__ (self) -> None :
        self.keys = ['Concept']

    def check_file(self ,dict_from_json ) :
        if len(dict_from_json) != 0 :
            return True
    
    def value_is_none (self , value) :
        if value == None :
            return True
    
    def parse_concept_value (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            try :
                if self.value_is_none(dict_from_json['Concept']) :
                    return None
                else :
                    return dict_from_json['Concept']
            except KeyError :
                return None
        else :
            return None

    def parse_concept (self , dict_from_json ) :
        if self.check_file(dict_from_json) :
            Concept = {}
            Concept['Name'] = self.parse_concept_value(dict_from_json)
            return Concept
        else :
            return None
    
    
    def parse_data (self , dict_from_json ) -> Any :
        return self.parse_concept(dict_from_json  )
    