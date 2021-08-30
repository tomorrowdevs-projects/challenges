def cleanUp(garden, bags, cap):
    clean = 'Clean'
    crap = 'Cr@p'
    dog = 'Dog!!'
    total_crap = 0
    # check the capacity of each bag
    total_cap = bags * cap

    # check the list inside the list garden
    for g in garden:
        # check if there's the Dog and stop the cycle by returning it
        if 'D' in g:
            return dog
        # count how many cr@p are there inside each list and sum all
        count_crap = g.count('@')
        total_crap += count_crap

    # if there isn't the dog I can check if the total capacity of the bags is enough to contain all the cr@p
    if total_cap >= total_crap:
        return clean
    else:
        return crap


if __name__ == '__main__':
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

    print(cleanUp(garden2, 2, 2))

"""
cleanUp(garden1, 2, 2) == 'Clean'
cleanUp(garden1, 1, 1) == 'Cr@p'
cleanUp(garden2, 2, 2) == 'Dog!!'
"""