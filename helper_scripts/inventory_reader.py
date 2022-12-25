from collections import defaultdict
from pprint import pprint

class InventoryParser():
    def __init__(self, inv_file):
        self.inv_dict = self.read_inv(inv_file)
    
    def read_inv(self, inv_file):
        dd = defaultdict(lambda: defaultdict(dict))
        in_section = 0
        with open(inv_file, 'r') as inventory:
            for line in inventory:
                line = line.replace('\n', '') if len(line) > 1 else '_'
                match tuple(line):
                    case ['[', *_, ':', 'v', 'a', 'r', 's', ']']:
                        cat = line.replace('[', '').replace(']', '').split(':')[0]
                        dd[cat]['vars'] = []
                        in_section = 'vars'
                    case ['[', *_, ']']:
                        cat = line.replace('[', '').replace(']', '')
                        dd[cat]['hosts'] = []
                        in_section = 'hosts'
                    case ['_']:
                        in_section = 0
                    case _ :
                        if in_section == 'hosts':
                            data = tuple([d for d in line.split(' ') if d])
                        elif in_section == 'vars':
                            data = line
                        dd[cat][in_section].append(data)
                        
        return dict(dd)

if __name__ == '__main__':
    inventory = '../inventory'
    parser = InventoryParser(inventory)
    pprint(parser.inv_dict)
