from collections import defaultdict
from pprint import pprint

class InventoryParser():
    def __init__(self, inv_file):
        self.inv_dict = self.read_inv(inv_file)
    
    def read_inv(self, inv_file):
        dd = defaultdict(list)
        with open(inv_file, 'r') as inventory:
            for line in inventory:
                line = line.replace('\n', '') if len(line) > 1 else '_'
                match tuple(line):
                    case ['[', *_, ']']:
                        cat = line.replace('[', '').replace(']', '')
                        dd[cat] = []
                    case ['_']:
                        continue
                    case _ :
                        dd[cat].extend(line.split(' '))
        return dict(dd)

if __name__ == '__main__':
    inventory = '../inventory'
    parser = InventoryParser(inventory)
    pprint(parser.inv_dict)
