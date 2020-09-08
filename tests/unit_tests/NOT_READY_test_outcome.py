import yaml
import re

from outcome import Outcome

def test_code_generation():
    
    #Create test outcome definition
    outcomeDefinition = yaml.safe_load('''
        - label:
            - Lead Time = 2 days
            - MTTR = 55 minutes
          value-point: Value Point 1
    ''')

    #Create outcome
    outcome = Outcome(outcomeDefinition[0])

    #Define regex for checking for outcome ids
    outcomeIdRegex = r'[0-9a-fA-F]{56}'
  
    assert re.match(r'"%s" \[label = "Lead Time = 2 days\nMTTR = 55 minutes", shape = "ellipse", fontname = "Courier New", style = "dashed", color = "#000000", fillcolor = "#dddddd", fontcolor = "#000000"\]\n"%s" -> "Value Point 1"' % (outcomeIdRegex, outcomeIdRegex), outcome.generate_code())

