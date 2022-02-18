from collections import Counter
import re

COMPONENT_RE = (
    r'('
        r'[A-Z][a-z]?'
        r'|'
        r'\([^(]+\)'
        r'|'
        r'\[[^[]+\]'
        r'|'
        r'\{[^}]+\}'
    r')'
    r'(\d*)'
)


def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts

molecule = "H2O"
molecule = "Mg(OH)2"
molecule = "K4[ON(SO3)2]2"
#molecule = "C6H12O6"
#molecule = "(C5H5)Fe(CO)2CH3"
#molecule = "{[Co(NH3)4(OH)2]3Co}(SO4)3"

print(parse_molecule(molecule))