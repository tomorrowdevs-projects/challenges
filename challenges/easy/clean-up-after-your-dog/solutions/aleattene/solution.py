"""
Python solution for challenge: "Clean up after your dog"
To test the function type from CLI: python tests.py
"""


def clean_up(garden, bags, cap):
    # Declaration of the variables (no use of the local constants according to the PEP-8 standard)
    dog, crap, clean = 'Dog!!', 'Cr@p', 'Clean'
    # Modify the list of lists in a single string
    garden = str(garden)
    # Check if the Dog is out
    if garden.count("D") > 0:
        return dog
    # Check if it is possible to clean the garden
    elif garden.count("@") > bags * cap:
        return crap
    # It is possible to clean the garden
    return clean
