import abc

class Parser(abc.ABC):

    def __init__(self, file):

        #Validate inputs
        try:
            self.file = file

        except:

            #Invalidate inputs
            self.file = None

            raise Exception('Parser has some invalid input parameters')

    @abc.abstractmethod
    def parse(self):
        pass
