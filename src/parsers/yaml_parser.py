import yaml

from parsers.parser import Parser

class YamlParser(Parser):

    def __init__(self, file):
        
        #Validate inputs
        try:
            self.file = file

        except:

            #Invalidate inputs
            self.file = None

            raise Exception('Parser has some invalid input parameters')

    def parse(self):
        
        #Parse yaml file
        yamlDocument = yaml.full_load(self.file)

        print(type(yamlDocument))
        print(type(yamlDocument['levels']))
        print(type(yamlDocument['levels'][0]))

        return(yamlDocument)