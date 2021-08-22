"""
Python solution for challenge: "Clean up after your dog"
To test the function type from CLI: python tests.py
"""


def clean_up(garden, bags, cap):
    # Total cleaning capacity
    total_cleaning_cap = bags * cap
    # Garden check
    for schema in garden:
        for char in schema:
            if char == "D":
                # Dog is out
                return 'Dog!!'
            elif char == "@":
                # Pick up cr@p
                total_cleaning_cap -= 1
    # Garden clean or not
    if total_cleaning_cap < 0:
        # Not enough cleaning capacity
        return 'Cr@p'
    else:
        # The garden was completely cleaned
        return 'Clean'
