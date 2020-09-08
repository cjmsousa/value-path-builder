import yaml

from valuepoint import ValuePoint

def test_code_generation():
    
    #Create test value point definition and configurations
    valuePointDefinition = yaml.safe_load('''
      - label: Value Point 1
        type: external
    ''')

    configurationDefinition = yaml.safe_load('''
        internal-color: "#1155cc"
        external-color: "#f22800"
    ''')

    #Create value point
    valuePoint = ValuePoint(valuePointDefinition[0], configurationDefinition)

    assert valuePoint.generate_code() == '"Value Point 1" [shape = "rectangle", fontname = "Courier New", style = "filled", fillcolor = "#f22800", color = "#ffffff", fontcolor = "#ffffff"]\n'

