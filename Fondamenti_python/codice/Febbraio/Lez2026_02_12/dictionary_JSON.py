"""Dictionary JSON"""

import json

menu = {
    'pizza' : 2.5,
    'panino' : 4.0,
    'bibita' : 2.5,
    'acqua' : 1.0,
    'caffe' : 1.3
}

print(json.dumps(menu, ensure_ascii=True))


with open("scontrino.json", "w") as f:
    print(json.dump(menu, f , indent=4))