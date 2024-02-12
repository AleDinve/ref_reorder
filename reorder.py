'''
@author: Giuseppe Alessio D'Inverno
@date: February 12, 2024

'''

import bibtexparser
from bibtexparser.library import Library

def reorder(name):
    ordered_list = []
    ordered_dict = {}
    with open(name) as f:
        library = bibtexparser.parse_string(f.read())
    for entry in library.entries:
        ordered_list.append({'key': entry.key, 'entry':entry})
        
        ordered_dict[entry.key] = entry
    ordered_dict = dict(sorted(ordered_dict.items(), key=lambda item: item[0].lower()))
    new_lib = Library()
    for key in ordered_dict:
        new_lib.add(ordered_dict[key])
    bibtexparser.write_file("references.txt", new_lib)


if __name__ == '__main__':
    reorder('references.txt')

