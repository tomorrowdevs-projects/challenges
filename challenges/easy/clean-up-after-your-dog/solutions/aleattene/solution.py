"""
garden1 = [
    ['_', '_', '_', '_', '_', '_'],
    ['_', '_', '_', '_', '@', '_'],
    ['@', '_', '_', '_', '_', '_']
]

garden2 = [
    ['_', '_', '_', '_'],
    ['_', '_', '_', '_'],
    ['@', '_', '_', 'D']
]
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


"""
# TEST CASES
print(clean_up(garden1, 2, 2) == 'Clean')
print(clean_up(garden1, 1, 1) == 'Cr@p')
print(clean_up(garden2, 2, 2) == 'Dog!!')
print(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 2, 2) == 'Clean')
print(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '@'], ['_', '_', '@', '_']], 1, 1) == 'Cr@p')
print(clean_up([['_', '_'], ['D', '_'], ['_', '_']], 2, 2) == 'Dog!!')
print(clean_up([['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_']], 2, 2) == 'Clean')
print(clean_up([['@', '@'], ['@', '@'], ['@', '@']], 2, 2) == 'Cr@p')
print(clean_up([['_', '_', '_', '_', 'D', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '@', '@', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', 'D', '_', '_']], 9, 5) == 'Dog!!')
print(clean_up([['_', '_', '_', '_', '_']], 6, 9) == 'Clean')
print(clean_up([['_', '_', 'D', '_', '_', '_', '_', '_', 'D'],
                ['_', '_', 'D', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '@', '_', '_', '_']], 4, 4) == 'Dog!!')
print(clean_up([['_', '@', '@'], ['_',' @', '@']], 1, 2) == 'Cr@p')
print(clean_up([['_', '_', '_', '_', '_', '_', '_', '@'], ['_', '_', '_', '@', 'D', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', 'D', '_'], ['_', '_', '_', '_', 'D', '_', '_', '_'],
                ['_', '_', '_', '_', 'D', '@', '_', '_']], 1, 6) == 'Dog!!')
print(clean_up([['_', '_', '_', '_', '_', '_', '_', '@', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '@', '_']], 4, 3) == 'Clean')
print(clean_up([['_', '_', '_', '_', '_']], 6, 0) == 'Clean')
print(clean_up([['_', '@', '@', '_', '_', '@', '_', '_', '_']], 4, 0) == 'Cr@p')
print(clean_up([['D', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'],
                ['_', '_', '@', '_'], ['_', '_', '_', '_']], 7, 8) == 'Dog!!')
print(clean_up([['_', '@', '_'], ['_', '@', '_']], 0, 8) == 'Cr@p')
"""