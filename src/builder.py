import os
import tempfile

from parsers.parser_factory import ParserFactory

from value_path.valuepoint import ValuePoint
from value_path.dependecy import Dependency
from value_path.comment import Comment


class Builder:

    def __init__(self, file, filename):

        #Validate inputs
        try:
            self.file = file
            self.filename = filename

        except:

            #Invalidate inputs
            self.file = None
            self.filename = None

            raise Exception('Builder has some invalid input parameters')

    def build(self):

        #Create parser based on file extension and parse file
        parser = ParserFactory.create_instance(os.path.splitext(self.filename)[1][1:], self.file)
        document = parser.parse()

        #Create configuration
        configuration = document['configuration'] if 'configuration' in document else None

        #Create output file
        f = tempfile.NamedTemporaryFile(mode="w", delete=False)

        #Start dot file
        f.write('digraph valuePath {\n')

        #Iterated levels in order
        for level in document['levels']:

            #Iterate value points
            for valuePointDefinition in level['value-points']:

                #Create value point
                valuePoint = ValuePoint(valuePointDefinition, configuration)
                f.write(valuePoint.generate_code())

        #Iterate dependencies
        for dependencyDefinition in document['dependencies']:

            #Create dependency
            dependency = Dependency(dependencyDefinition)
            f.write(dependency.generate_code())

        #Iterate comments
        comments = document['comments'] if 'comments' in document else []
        for commentDefinition in comments:

            #Create comment
            comment = Comment(commentDefinition)
            f.write(comment.generate_code())

        #Iterate levels
        levelOrderDot = ""
        levelId = 0
        for level in document['levels']:

            #Create level
            levelId, levelDot = self.create_level(levelId ,level)
            f.write(levelDot + '\n')

            levelOrderDot += '"%s" -> ' % levelId
            levelId += 1
        
        #Write level order
        f.write('edge [style = invis]\n')
        f.write(levelOrderDot[:-4] + '\n')

        #End dot file
        f.write('}\n')
        f.close()

        #Build graph image
        outputFile = tempfile.NamedTemporaryFile(mode="w", suffix=".svg", delete=False)
        os.system('dot -Tsvg %s -o %s' % (f.name, outputFile.name))

        return(outputFile.name)

    def create_level(self, levelId, level):

        #Define level definition
        levelDot =  'node [style = invis, shape = point] { rank = same; "%s"\n' % levelId

        #Iterate value points
        for valuePoint in level['value-points']:

            levelDot += '"%s"\n' %valuePoint['label']

        levelDot += '}'

        return(levelId, levelDot) 