import hashlib

class Comment:

    def __init__(self, commentDefinition):

        #Validate inputs
        try:
            self.label = commentDefinition['label']
            self.valuePoint = commentDefinition['value-point']

        except:

            #Invalidate inputs
            self.label = None

            raise Exception('Comment has some invalid input parameters')

    def generate_code(self):

        #Define comment definition
        commentId = hashlib.sha224(''.join(self.label).encode('utf-8')).hexdigest()
        commentText = '\n'.join(self.label)
        commentCode = '"%s" [label = "%s", shape = "ellipse", fontname = "Courier New", style = "dashed", color = "#000000", fillcolor = "#dddddd", fontcolor = "#000000"]\n' % (commentId, commentText)   
        commentCode += '"%s" -> "%s"\n' % (commentId, self.valuePoint)
        
        return(commentCode)