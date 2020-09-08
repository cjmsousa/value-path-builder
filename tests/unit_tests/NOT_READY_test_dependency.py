import yaml

# pylint: disable=import-error
from dependecy import Dependency

def test_code_generation():
    
    #Create test dependecy definition
    dependencyDefinition = yaml.safe_load('''
      - src: Value Point 1
        dest: Value Point 2
    ''')

    #Create dependency
    dependency = Dependency(dependencyDefinition[0])

    assert dependency.generate_code() == '"Value Point 1" -> "Value Point 2"\n'

