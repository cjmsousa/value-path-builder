from parsers.vpb_parser import VpbParser
from parsers.yaml_parser import YamlParser

class ParserFactory:

    #Define list of available parsers
    PARSERS = ['vpb', 'yaml']

    @staticmethod
    def create_instance(parserType, file):

        if parserType in ParserFactory.PARSERS:
            
            # I'll do this dynamically when I'm in the mood :)
            #type(parserType, (), {})(file)
            
            #Create the proper parser 
            if (parserType) == "yaml": return YamlParser(file)
            if (parserType) == "vpb": return VpbParser(file)
            
        else:
            #Raise the proper exception
            raise Exception("[%s] is an invalid parser type" %(parserType))