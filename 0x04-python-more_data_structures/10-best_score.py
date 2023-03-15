#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        biggest = max(a_dictionary.values())
        for keys in a_dictionary:
            if biggest == a_dictionary[keys]:
                return keys
