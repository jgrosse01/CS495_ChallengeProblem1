"""
Author:         Jake Grosse
Created:        6 February 2022
Description:    Lookup library for CS495 Challenge Problems.
"""


# function to lookup a license plate prefix given a list of license plates
def lookup_prefix(search_term: int, license_index: list) -> bool and dict:
    # for each entry in the list, search for the plate prefix passed in
    for entry in license_index:
        if entry['License Plate Prefix'] == str(search_term):
            result = entry
            # compound return for whether the result was found and the result
            return True, result
    # if entry was not found to match, return False and None
    return False, None
