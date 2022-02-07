"""
Author:         Jake Grosse
Created:        6 February 2022
Description:    The main loop for the text-based Montana License Prefix Lookup problem for CS495 Challenge 1.
"""

from mt_license_lib.FileInterface import *
from mt_license_lib.Lookup import *

# main license plate lookup loop
if __name__ == '__main__':
    # load in the CSV file
    license_registry = read_csv()

    # welcome statement
    print("Welcome to Montana License Lookup!")

    # determine what they want displayed
    while True:
        # prompt user
        print("Would you like to know the County, Seat City, or Both from your searches? " +
              "Select the corresponding number: ")
        print("\t1. County Only.")
        print("\t2. Seat City Only.")
        print("\t3. Both County and Seat City.")
        print("\t4. Exit Program (This will stop this application).")
        # get input
        print_spec = input("Selection: ")

        # if they select exit, exit
        if print_spec == "4":
            exit(0)

        # list for validation
        valid_selections = [1, 2, 3, 4]

        # try to convert to int, if impossible prompt again for valid input
        try:
            print_spec = int(print_spec.strip())
        except:
            print("Please input a valid selection. (Only the number, as an integer, no punctuation).")
            continue

        # if the number is out of bounds, prompt again for valid input
        if print_spec not in valid_selections:
            # prompt and return to top of loop
            print("Please input one of the selections specified (numbers 1-4).")
            continue
        else:
            # break loop if input is valid
            break

    # main search loop
    while True:
        # prompt for search key
        prefix = input("Please Enter an Integer License Prefix (input -1 to exit): ")
        try:
            # try to convert to an integer
            prefix = int(prefix.strip())
        except:
            # if not an integer, return to start of the loop
            print("Please Enter an INTEGER. Do not add any other characters.")
            continue

        # if user specifies to exit, exit
        if prefix == -1:
            exit(0)

        # lookup the prefix and get boolean then the entry
        found_entry, entry = lookup_prefix(prefix, license_registry)

        # if there is no corresponding entry inform the user
        if not found_entry:
            print("There is no valid entry for this license prefix.")
        # otherwise print response
        else:
            print(f'For the license plate prefix "{prefix}":')
            if print_spec == 1 or print_spec == 3:
                print(f"\tThe county is \"{entry['County']}\".")
            if print_spec == 2 or print_spec == 3:
                print(f"\tThe seat city is \"{entry['County Seat']}\".")
