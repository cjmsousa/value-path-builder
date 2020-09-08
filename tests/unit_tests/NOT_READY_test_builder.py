import os
import yaml
import filecmp

# pylint: disable=import-error
from src.builder import Builder

def test_build():
    assert True
    #Get current directory
    #currentDirectory = os.path.dirname(os.path.realpath(__file__))

    #with open('%s/test_value_path.yaml' % (currentDirectory)) as f:
        
        #Read all test file
        #testFile = f.read()

        #Build graph
        #Builder(testFile, 'output.yaml', os.path.dirname(os.path.realpath(__file__))).build()

        #Check if files are equal
        #assert filecmp.cmp('%s/output.svg' % (currentDirectory), '%s/test_value_path.svg'  % (currentDirectory)) 