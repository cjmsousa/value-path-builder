class ValuePoint:

    def __init__(self, valuePointDefinition, configuration):

        #Validate inputs
        try:
            self.label = valuePointDefinition['label']
            self.type = valuePointDefinition['type']
            self.configuration = configuration

        except:

            #Invalidate inputs
            self.label = None
            self.type = None
            self.configuration = None

            raise Exception('Value Point has some invalid input parameters')

    def generate_code(self):


        #Define value point definition
        print(self.configuration)
        print(self.type)
        print(self.configuration[self.type])
        print(self.configuration[self.type]['color'])
        fillColor = self.configuration[self.type]['color']
        fontColor = "#ffffff"
        valuePointCode = '"%s" [shape = "rectangle", fontname = "Courier New", style = "filled", fillcolor = "%s", color = "#ffffff", fontcolor = "%s"]\n' % (self.label, fillColor, fontColor)
    
        return(valuePointCode)