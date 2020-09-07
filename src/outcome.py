import hashlib

class Outcome:

    def __init__(self, outcomeDefinition):

        #Validate inputs
        try:
            self.label = outcomeDefinition['label']
            self.valuePoint = outcomeDefinition['value-point']

        except:

            #Invalidate inputs
            self.label = None

            raise Exception('Outcome has some invalid input parameters')

    def generate_code(self):

        #Define outcome definition
        outcomeId = hashlib.sha224(''.join(self.label).encode('utf-8')).hexdigest()
        outcomeText = '\n'.join(self.label)
        outcomeCode = '"%s" [label = "%s", shape = "ellipse", fontname = "Courier New", style = "dashed", color = "#000000", fillcolor = "#dddddd", fontcolor = "#000000"]\n' % (outcomeId, outcomeText)   
        outcomeCode += '"%s" -> "%s"\n' % (outcomeId, self.valuePoint)
        
        return(outcomeCode)