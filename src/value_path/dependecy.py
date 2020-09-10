class Dependency:

    def __init__(self, dependecyDefinition):

        #Validate inputs
        try:
            self.source = dependecyDefinition['src']
            self.destination = dependecyDefinition['dest']

        except:

            #Invalidate inputs
            self.source = None
            self.destination = None

            raise Exception('Dependency has some invalid input parameters')

    def generate_code(self):

        #Define dependecy definition
        dependencyCode = '"%s" -> "%s"\n' % (self.source, self.destination)
    
        return(dependencyCode)