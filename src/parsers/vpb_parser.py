import yaml

from parsers.parser import Parser

class VpbParser(Parser):

    def __init__(self, file):

        #Call base class constructor
        super().__init__(file)

    def parse(self):
        
        #Parse yaml file
        vpbDocument = yaml.full_load(self.file)

        #####################################################################
        #This is a dumb way of doing this. I'll get here to refactor
        #####################################################################

        #Get configuration part
        document = dict()
        document['configuration'] = self.parse_configuration(vpbDocument)
        document['levels'] = self.parse_levels(vpbDocument)
        document['dependencies'] = self.parse_dependencies(vpbDocument)
        document['comments'] = self.parse_comments(vpbDocument)

        return(document)

    def parse_configuration(self, vpbDocument):

        return(vpbDocument['configuration'])

    def parse_levels(self, vpbDocument):

        newLevels = list()
        for level in vpbDocument['levels']:
            
            newLevel = dict()
            newValuePoints = list()
            for valuePoint in level['value-points']:

                newValuePoint = dict()
                newValuePoint['label'] = valuePoint['label']
                newValuePoint['type'] = valuePoint['type']

                newValuePoints.append(newValuePoint)            

            newLevel['value-points'] = newValuePoints
            newLevels.append(newLevel)

        return(newLevels)

    def parse_dependencies(self, vpbDocument):
        
        newDependencies = list()
        for level in vpbDocument['levels']:

            for valuePoint in level['value-points']:

                if 'dependencies' in valuePoint:

                    for dependency in valuePoint['dependencies']:

                        newDependency = dict()
                        newDependency['src'] = dependency
                        newDependency['dest'] = valuePoint['label']

                        newDependencies.append(newDependency)

        return(newDependencies)

    def parse_comments(self, vpbDocument):

        newComments = list()
        for level in vpbDocument['levels']:

            for valuePoint in level['value-points']:
                
                if 'comment' in valuePoint:
                    
                    newComment = dict()

                    newComment['label'] = valuePoint['comment']
                    newComment['value-point'] = valuePoint['label']

                    print("newComment %s" %(str(valuePoint['comment'])))
                    newComments.append(newComment)

        return(newComments)